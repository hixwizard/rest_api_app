from rest_framework import viewsets, status, mixins, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from api.serializers import (PostSerializer, GroupSerializer,
                             CommentSerializer, FollowSerializer)
from posts.models import Post, Group, Follow
from api.permissions import IsOwnerOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    """Набор отображений для постов."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """Набор отображений для групп."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CommentViewSet(viewsets.ModelViewSet):
    """Набор отображений для комментариев."""
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments.all()

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)


class FollowViewSet(
    mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def list(self, request):
        queryset = FollowSerializer(user=request.user)
        serializer = FollowSerializer(queryset, many=True)
        return Response(serializer.data)

    def follow(self, request):
        serializer = FollowSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data['user'] == request.user:
                return Response(
                    'Вы не можете быть подписанным на самого себя.',
                    ststus=status.HTTP_400_BAD_REQUEST
                )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, satus=status.HTTP_400_BAD_REQUEST)
