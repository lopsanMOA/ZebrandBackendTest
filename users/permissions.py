from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            print("es aca")
            return True
        print("no aca")
        print(request.user.is_authenticated )
        print(request.user.is_admin)
        return request.user.is_authenticated and request.user.is_admin


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin