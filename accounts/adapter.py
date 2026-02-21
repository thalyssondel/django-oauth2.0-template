from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.core.exceptions import PermissionDenied
from django.contrib.auth.backends import ModelBackend

class BlockAdminAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user

        if user and user.pk:
            if user.is_superuser or user.is_staff:
                raise PermissionDenied("This account could not be authenticated at this time")
            

class BanCheckBackend(ModelBackend):
    def authenticate(self, request, username = None, password = None, **kwargs):
        user = super().authenticate(request, username, password, **kwargs)

        if user and getattr(user, 'is_banned', False):
            raise PermissionDenied('Your account is banned')
        return user