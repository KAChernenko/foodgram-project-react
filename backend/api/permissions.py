from rest_framework import permissions


class IsAdminAuthorOrReadOnly(permissions.BasePermission):
    """Разрешение для администратора/автора"""

    def has_object_permission(self, request, view, obj):
        # Разрешить все операции чтения анонимным пользователям
        if (request.method in permissions.SAFE_METHODS
           and not request.user.is_authenticated):
            return True

        # Ограничить операции записи только администраторам и авторам
        return (
            request.user.is_authenticated
            and (request.user.is_superuser
                 or request.user == obj.author)
        )
