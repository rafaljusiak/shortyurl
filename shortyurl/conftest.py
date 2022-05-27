from typing import Any

import pytest
from django.test import Client

from shortyurl.urls.models import Url, Redirect


@pytest.fixture
def client() -> Client:
    return Client()


@pytest.fixture
def url(db: Any) -> Url:
    return Url.objects.create(
        original_url="https://google.com",
        alias="aaaaaa",
    )


@pytest.fixture
def redirect(url: Url) -> Redirect:
    return Redirect.objects.create(
        url=url,
        ip="8.8.8.8",
    )
