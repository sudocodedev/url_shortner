from datetime import datetime, timedelta

from rest_framework import serializers

from common.helpers import encode_digit
from common.models import COMMON_CHAR_MAX_LENGTH
from services import CounterService
from shorten.models import URLMapping


class URLShortenCUDSerializer(serializers.ModelSerializer):
    """CUD Serializer for URL shortening"""

    url = serializers.URLField(max_length=COMMON_CHAR_MAX_LENGTH, required=True)

    class Meta:
        model = URLMapping
        fields = ["url"]

    def create(self, validated_data):
        """
        - Creates URLMapping instance with the validated_data
        - If short_code is null, generate short_code and save it
        - If expirt_tm is not present, set it to 2 days from now and save it.
        """
        instance = super().create(validated_data)
        if not instance.short_code:
            num = CounterService.fetch_value("url_shortner", "next")
            instance.short_code = encode_digit(digit=num)

        if not instance.expiry_tm:
            instance.expiry_tm = datetime.now() + timedelta(days=2)

        instance.save()
        return instance


class URLShortenRetrieveSerializer(serializers.ModelSerializer):
    """Retrieve Serializer for URLMapping instance"""

    class Meta:
        model = URLMapping
        fields = ["id", "uuid", "url", "short_code", "created", "modified"]

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError


class URLShortenStatsSerializer(serializers.ModelSerializer):
    """Serializer to fetch stats for respective URLMapping instance"""

    class Meta:
        model = URLMapping
        fields = ["url", "short_code", "expiry_tm", "access_count", "last_accessed"]

    def create(self, validated_data):
        raise NotImplementedError

    def update(self, instance, validated_data):
        raise NotImplementedError
