"""Logs the information from BASE_DIR/.release.

To use, add to INSTALLED_APPS:

    INSTALLED_APPS = [
        ...
        'release_info',
    ]

Then you'll see a log message describing the current `tag` every time Django boots.
"""
from logging import getLogger

from django.apps import AppConfig
from django.conf import settings

default_app_config = "release_info.ReleaseAppConfig"

logger = getLogger(__name__)

class ReleaseAppConfig(AppConfig):
    name = "release_info"

    def ready(self):
        if not settings.DEBUG:
            logger.info(f"init AppConfig.ready(): {settings.RELEASE_TAG}")
