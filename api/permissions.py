from rest_framework import permissions

class IsOperatorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        # Allow GET, HEAD, OPTIONS (read-only) for all
        if request.method in permissions.SAFE_METHODS:
            return True
        # Allow write operations only for users in 'Operators' group
        return request.user.is_authenticated and request.user.groups.filter(name='Operators').exists()