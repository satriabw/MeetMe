from rest_framework import permissions


class UserPermissionsAll(permissions.BasePermission):


    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        else:
            return False


class UserProfilePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return request.user.id is obj.user.id

class UserInterestPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == "POST"

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True

class UserInterestDetailPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_staff:
            return True
        return obj.user.user.id == request.user.id
