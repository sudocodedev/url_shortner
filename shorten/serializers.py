from rest_framework import serializers

from shorten.models import URLMapping


class URLShortenCUDSerializer(serializers.ModelSerializer):
    """CUD Serializer for URL shortening"""

    class Meta:
        model = URLMapping
        fields = ["url"]


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
