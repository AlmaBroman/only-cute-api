from rest_framework import serializers
from posts.models import Post
from likes.models import Like
from saved_posts.models import SavedPost


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()
    saved_post_id = serializers.SerializerMethodField()
    image =  image = serializers.ImageField(required=False, allow_null=True)

    def validate_image(self, value):
        """
        Image validation, checks if the image
        is too big.
        The default picture is read as a string value,
        and therefore can't be run through the validator,
        so first we check if the value is a string,
        if it is it gets returned without having to pass 
        the size, width and height validations.
        without this we get an error message when trying to upload
        image without submitting a picture
        """
        if not isinstance(value, str):
            if value.size > 1024 * 1024 * 2:
                raise serializers.ValidationError('Image size larger than 2MB!')
            if value.image.height > 4096:
                raise serializers.ValidationError(
                    'Image height larger than 4096px!'
                )
            if value.image.width > 4096:
                raise serializers.ValidationError(
                    'Image width larger than 4096px!'
                )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    def get_saved_post_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            saved_post = SavedPost.objects.filter(
                owner=user, post=obj
            ).first()
            return saved_post.id if saved_post else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'like_id',
            'likes_count', 'comments_count', 'saved_post_id',
        ]