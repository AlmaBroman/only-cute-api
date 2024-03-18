from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    """
    Post Serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        """
        True when the request user is equal to the owner of the profile
        """
        request = self.context['request']
        return request.user == obj.owner
    
    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image',
        ]
