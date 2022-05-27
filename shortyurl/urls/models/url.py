from django.conf import settings
from django.db import models
from rest_framework.reverse import reverse

from shortyurl.common.models import BaseModel


class Url(BaseModel):
    alias = models.CharField(
        max_length=16,
        unique=True,
    )
    original_url = models.URLField()

    @property
    def redirect_url(self):
        path = reverse("urls-detail", args=(self.alias,))
        return f"{settings.REDIRECT_DOMAIN}{path}"

    @property
    def redirects_count(self) -> int:
        return self.redirects.count()

    def __str__(self) -> str:
        return f"{self.alias} -> {self.original_url}"

    class Meta:
        default_related_name = "urls"
