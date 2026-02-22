from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.core.exceptions import PermissionDenied
from allauth.account.adapter import DefaultAccountAdapter

import logging

logger = logging.getLogger('accounts')

class BlockAdminAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user

        if user and user.pk:
            if user.is_superuser or user.is_staff:
                logger.warning(f"⚠️ SECURITY: Admin social login blocked for: {user.email}")
                raise PermissionDenied("This account could not be authenticated at this time")
            
            if getattr(user, 'is_banned', False):
                logger.info(f"🚫 BANNED: Banned user's social login attempt blocked for: {user.email}")
                raise PermissionDenied("Your account has been banned")

class BlockAccountAdapter(DefaultAccountAdapter):
    def pre_login(self, request, user, **kwargs):
        if getattr(user, 'is_banned', False):
            logger.info(f"🚫 BANNED: Banned user's standard login attempt blocked for: {user.email}")
            raise PermissionDenied("Your account has been banned")