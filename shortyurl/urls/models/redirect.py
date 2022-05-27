from django.db import models

from shortyurl.common.models import BaseModel


class Redirect(BaseModel):
    url = models.ForeignKey(
        "urls.Url",
        on_delete=models.CASCADE,
    )
    ip = models.GenericIPAddressField(
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return super().__str__()

    class Meta:
        default_related_name = "redirects"
