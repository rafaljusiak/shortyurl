from shortyurl.urls.models import Url, Redirect


def test_redirects_count_empty(url: Url):
    assert url.redirects_count == 0


def test_redirects_count_existing_redirect(url: Url, redirect: Redirect):
    assert url.redirects_count == 1
