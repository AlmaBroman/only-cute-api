from django.contrib.auth.models import User
from django.test import TestCase
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from posts.models import Post
from likes.models import Like
from comments.models import Comment


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='alex', password='pass')

    def test_can_list_posts(self):
        alex = User.objects.get(username='alex')
        Post.objects.create(owner=alex, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='alex', password='pass')
        response = self.client.post('/posts/', {'title': 'a title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post('/posts/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        alex = User.objects.create_user(username='alex', password='pass')
        molly = User.objects.create_user(username='molly', password='pass')
        Post.objects.create(
            owner=alex, title='alex title', content='alexs content'
        )
        Post.objects.create(
            owner=molly, title='mollys title', content='mollys content'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'alex title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_post(self):
        self.client.login(username='alex', password='pass')
        response = self.client.put('/posts/1/', {'title': 'a new title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_post(self):
        self.client.login(username='molly', password='pass')
        response = self.client.put('/posts/1/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostLikesTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user', password='password123'
            )
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(
            owner=self.user, title='Test Post', content='Test Content'
            )

    def test_post_has_number_of_likes(self):
        existing_like = Like.objects.filter(
            owner=self.user, post=self.post
            ).exists()

        if not existing_like:
            Like.objects.create(owner=self.user, post=self.post)

        response = self.client.get(f'/posts/{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['likes_count'], 1)


class PostCommentsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user', password='password123'
            )
        self.client.force_authenticate(user=self.user)
        self.post = Post.objects.create(
            owner=self.user, title='Test Post', content='Test Content'
            )

    def test_post_has_number_of_comments(self):
        for i in range(5):
            Comment.objects.create(
                owner=self.user, post=self.post, content=f'Test Comment {i}'
                )

        response = self.client.get(f'/posts/{self.post.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['comments_count'], 5)


class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='password123')
        self.post = Post.objects.create(owner=self.user, title='Test Post', content='Test Content')

    def test_article_string_representation(self):
        expected_representation = f'{self.post.id} {self.post.title}'
        self.assertEqual(str(self.post), expected_representation)