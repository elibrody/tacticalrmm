"""
Copyright (c) 2024-present Amidaware Inc.
This file is subject to the EE License Agreement.
For details, see: https://license.tacticalrmm.com/ee
"""

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialApp
from django.core.exceptions import PermissionDenied

from accounts.models import Role
from core.utils import token_is_valid
from tacticalrmm.logger import logger
from tacticalrmm.utils import get_core_settings


class TacticalSocialAdapter(DefaultSocialAccountAdapter):

    def populate_user(self, request, sociallogin, data):
        _, valid = token_is_valid()
        if not valid:
            raise PermissionDenied()

        user = super().populate_user(request, sociallogin, data)
        try:
            provider = sociallogin.account.get_provider()
            provider_settings = SocialApp.objects.get(provider_id=provider).settings
            user.role = Role.objects.get(pk=provider_settings["role"])
        except Exception:
            logger.debug(
                "Provider settings or Role not found. Continuing with blank permissions."
            )
        return user

    def list_providers(self, request):
        core_settings = get_core_settings()
        if not core_settings.sso_enabled:
            return []

        return super().list_providers(request)
