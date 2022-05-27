from django.http import HttpRequest
from ipware import get_client_ip

from shortyurl.urls.models import Redirect, Url


def save_redirect(request: HttpRequest, url: Url) -> Redirect:
    ip, _ = get_client_ip(request)
    return Redirect.objects.create(url=url, ip=ip)
