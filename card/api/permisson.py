from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


class MyPermissons(permissions.BasePermission):
    print('permisdson isledi')
    def has_permission(self, request, view):
        print(request.user,IsAuthenticated)
        if request.method in permissions.SAFE_METHODS and request.user.is_authenticated:
            return True
        # return super().has_permission(request, view)