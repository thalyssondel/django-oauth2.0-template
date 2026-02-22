from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import PermissionDenied


class BanCheckBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        user = super().authenticate(request, username, password, **kwargs)

        if user and getattr(user, "is_banned", False):
            raise PermissionDenied("Your account has been banned")
        return user
