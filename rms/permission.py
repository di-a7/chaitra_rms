from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

class IsAuthenticatedOrReadonly(BasePermission):
   def has_permission(self, request, view):
      return request.method in SAFE_METHODS or request.user and request.user.is_authenticated