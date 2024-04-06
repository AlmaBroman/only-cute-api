from django.test import TestCase
from .models import Profile
from django.contrib.auth.models import User

class TestProfileModel(TestCase):
    """
    Tests for the Profile Model
    """

    def setUp(self):
        self.user = User.objects.create_user(
            username='test_user', password='password123'
            )
        # Create a profile if it doesn't already exist
        if not Profile.objects.filter(owner=self.user).exists():
            Profile.objects.create(
                owner=self.user, name='Test Profile', content='Test Content'
                )

    def test_profile_created(self):
        # Check if a profile was created for the user
        profile = Profile.objects.get(owner=self.user)

        # Assert that a profile was created for the user
        self.assertTrue(profile)

    def test_image_defaults_to_placeholder(self):
        # Retrieve the profile created in setUp
        profile = Profile.objects.get(owner=self.user)

        # Check if the default placeholder image is assigned
        default_image_url = '../default-profile_rgasqm'
        self.assertTrue(profile.image.url.endswith(default_image_url))

    def test_article_string_representation(self):
        profile = Profile.objects.get(owner=self.user)
        self.assertEqual(str(profile), "test_user's profile")
