from rest_framework import permissions


class IsInstructorOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        
        return (
            request.user.is_superuser or 
            request.user.is_staff or 
            request.user.has_perm('courses.can_create_courses')
        )