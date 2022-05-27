from typing import NoReturn, Any

import pytest

from django.conf import settings
from django.test import override_settings

from shortyurl.urls.models import Url
from shortyurl.urls.utils.alias import is_alias_unique, generate_random_url_alias


@pytest.mark.parametrize(
    "increase_default_length",
    [
        pytest.param(True, id="increase-default-value-by-1"),
        pytest.param(False, id="use-default-value"),
    ],
)
def test_generate_random_url_alias_has_length_taken_from_settings(
    db: Any, increase_default_length: bool
) -> None:
    expected_length = settings.ALIAS_MINIMUM_LENGTH
    if increase_default_length:
        expected_length += 1

    with override_settings(ALIAS_MINIMUM_LENGTH=expected_length):
        alias = generate_random_url_alias()
        assert type(alias) is str
        assert len(alias) == expected_length


def test_is_alias_unique_returns_true_for_unique_alias(url: Url) -> NoReturn:
    assert is_alias_unique(url.alias + "a") is True


def test_is_alias_unique_returns_false_for_existing_alias(url: Url) -> NoReturn:
    assert is_alias_unique(url.alias) is False
