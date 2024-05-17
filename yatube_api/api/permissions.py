from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Пользователь может редактировать или удалять только свои объекты.
    """
    def has_object_permission(self, request, view, obj):
        if (request.method in permissions.SAFE_METHODS
           or obj.author == request.user):
            return True
        return False
