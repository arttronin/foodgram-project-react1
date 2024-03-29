from rest_framework import permissions


class IsAuthorOrReadOnlyPermission(permissions.BasePermission):
    """Только владельцам объекта может редактировать его."""
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    """Авторизованные пользователи могут смотреть страницы пользователей
    """
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (request.method in permissions.SAFE_METHODS
                and request.user.is_staff or request.user.is_superuser)
        )
