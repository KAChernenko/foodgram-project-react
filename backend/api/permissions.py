from rest_framework import permissions


class IsAdminAuthorOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """Разрешение дминистратору/автору"""

    def has_object_permission(self, request, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or (request.user == obj.author)
            or request.user.is_staff
        )
