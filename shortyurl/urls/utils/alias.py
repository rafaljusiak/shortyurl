import logging

from django.conf import settings
from django.utils.crypto import get_random_string

from shortyurl.urls.models import Url

logger = logging.getLogger(__name__)


def generate_random_url_alias(alias_length: int = None) -> str:
    """Returns a unique and random alias of the url"""
    alias_length = alias_length or settings.ALIAS_MINIMUM_LENGTH
    retry = 0

    while True:
        alias = get_random_string(length=alias_length)

        if is_alias_unique(alias):
            return alias
        else:
            retry += 1
            if retry % settings.ALIAS_GENERATION_MAX_RETRIES:
                logger.warning(
                    f"The number of attempts to generate a URL alias exceeded, perhaps the ALIAS_MINIMUM_LENGTH setting should be increased (current value is: {settings.ALIAS_MINIMUM_LENGTH})"
                )
                alias_length += 1


def is_alias_unique(alias: str) -> bool:
    """Verifies whether alias already exists"""
    return not Url.objects.filter(alias=alias).exists()
