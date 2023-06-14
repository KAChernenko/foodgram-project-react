from rest_framework import permissions


class IsAdminAuthorOrReadOnly(permissions.BasePermission):
    """Разрешение для администратора/автора"""

    def has_object_permission(self, request, view, obj):
        def has_object_permission(self, request, view, obj):
            return (request.method in permissions.SAFE_METHODS
                    or obj.author == request.user)
