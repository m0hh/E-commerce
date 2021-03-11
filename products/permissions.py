from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self,request,view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.seller == request.user


class IsOwner(permissions.BasePermission):
    def has_object_permission(self,request,view, obj):
        return obj.user == request.user

class IsProductOwner(permissions.BasePermission):
    def has_object_permission(self,request,view, obj):
        return obj.owner == request.user