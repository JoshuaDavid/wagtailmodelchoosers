from django.contrib.auth.models import Permission
from django.conf import settings

from rest_framework.permissions import BasePermission


class IsWagtailAdmin(BasePermission):

    @property
    def _permission(self):
        return Permission.objects.get(name=u'Can access Wagtail admin')

    def has_permission(self, request, view):
        return request.user.is_authenticated() and request.user.has_perm(self._permission)


class IsRegisteredModelChooserModel(BasePermission):

    def has_permission(self, request, view):
        params = request.parser_context.get('kwargs')
        app_name = params.get('app_name')
        model_name = params.get('model_name')

        model_path = u'{}.{}'.format(app_name, model_name)
        return model_path in self.configured_model_chooser_models()

    def configured_model_chooser_models(self):
        return [chooser['content_type'] for chooser in settings.MODEL_CHOOSERS_OPTIONS.values()]
