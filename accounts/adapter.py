from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.core.exceptions import PermissionDenied

class BlockAdminAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user

        if user and user.pk:
            if user.is_superuser or user.is_staff:
                raise PermissionDenied("This account could not be authenticated at this time")