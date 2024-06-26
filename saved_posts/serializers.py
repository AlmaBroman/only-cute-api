from django.db import IntegrityError
from rest_framework import serializers
from .models import SavedPost


class SavedPostSerializer(serializers.ModelSerializer):
    """
        Serializer for the Saved Post model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = SavedPost
        fields = ['id', 'created_at', 'owner', 'post']

        def create(self, validated_data):
            try:
                return super().create(validated_data)
            except IntegrityError:
                raise serializers.ValidationError({
                    'detail': 'possible duplicate'
                })
