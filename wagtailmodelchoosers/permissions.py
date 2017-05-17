from django.contrib.auth.models import Permission

from rest_framework.permissions import BasePermission


class IsWagtailAdmin(BasePermission):

    @property
    def _permission(self):
        return Permission.objects.get(name=u'Can access Wagtail admin')

    def has_permission(self, request, view):
        return request.user.is_authenticated() and request.user.has_perm(self._permission)
