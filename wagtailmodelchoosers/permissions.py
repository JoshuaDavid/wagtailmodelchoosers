from django.contrib.auth.models import Permission
from django.conf import settings

from rest_framework.permissions import BasePermission


class IsWagtailAdmin(BasePermission):

    @property
    def _permission(self):
        return u'wagtailadmin.access_admin'

    def has_permission(self, request, view):
        return request.user.is_authenticated() and request.user.has_perm(self._permission)


class IsRegisteredModelChooserModel(BasePermission):

    def has_permission(self, request, view):
        params = request.parser_context.get('kwargs')
        chooser_name = params.get('chooser')
        return chooser_name in settings.MODEL_CHOOSERS_OPTIONS
