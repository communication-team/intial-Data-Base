  
from rest_framework import permissions

class PermissionsClass(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Admin Permissions IsAuthenticatedOrReadOnly
        # if request.user.id == obj.user_id:
        #     return True
        # # READ ONLY
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # # Write Permission for author of blog
        # if request.user == obj.publisher:
        #     return True
             # Read Only permissions
        if request.method in permissions.SAFE_METHODS:
            return True
        # If the logged in user same as the author
        # Write persmission
        return obj.id_user == request.user
        # return obj.id_info.id_user == request.user
        # return request.owner == obj.author  