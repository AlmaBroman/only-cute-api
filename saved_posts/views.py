from rest_framework import generics, permissions
from only_cute_api.permissions import IsOwnerOrReadOnly
from .models import SavedPost
from .serializers import SavedPostSerializer


class SavedPostList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SavedPostSerializer
    queryset = SavedPost.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SavedPostDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SavedPostSerializer
    queryset = SavedPost.objects.all()
