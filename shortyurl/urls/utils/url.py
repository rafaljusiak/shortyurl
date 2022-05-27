from shortyurl.urls.models import Url
from shortyurl.urls.utils.alias import generate_random_url_alias


def create_short_url(url: str) -> Url:
    alias = generate_random_url_alias()
    url = Url.objects.create(
        alias=alias,
        original_url=url,
    )
    return url
