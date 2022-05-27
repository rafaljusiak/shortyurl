from rest_framework import serializers

from shortyurl.urls.models import Url
from shortyurl.urls.utils.url import create_short_url


class UrlSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return create_short_url(validated_data["original_url"])

    class Meta:
        model = Url
        fields = (
            "id",
            "alias",
            "created_at",
            "original_url",
            "redirect_url",
            "redirects_count",
        )
        extra_kwargs = {
            "alias": {"read_only": True},
        }
