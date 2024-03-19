from rest_framework import generics, permissions
from only_cute_api.permissions import IsOwnerOrReadOnly
from .models import SavePost
from .serializers import SavePostSerializer

class SavePostList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SavePostSerializer
    queryset = SavePost.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SavePostDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SavePostSerializer
    queryset = SavePost.objects.all()
