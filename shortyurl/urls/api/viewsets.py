from rest_framework import viewsets, mixins

from shortyurl.urls.api.serializers import UrlSerializer
from shortyurl.urls.models import Url
from shortyurl.urls.utils.redirect import save_redirect


class UrlViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    lookup_field = "alias"
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        save_redirect(request, self.get_object())
        return response
