  
from rest_framework import permissions

class PermissionsClass(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Admin Permissions
        if request.user.id == 1:
            return True
        # READ ONLY
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write Permission for author of blog
        if request.user == obj.publisher:
            return True