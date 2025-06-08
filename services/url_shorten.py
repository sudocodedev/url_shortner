from django.db import transaction
from rest_framework.exceptions import ValidationError

from shorten.models import URLMapping
from shorten.serializers import URLShortenCUDSerializer


class URLShortenService:
    """Service layer for managing shortened URLs."""

    @staticmethod
    def get(code: str, fetch: bool = False):
        """
        - Retrieve an active URL mapping by short code.
        - If `fetch` flag is True, update access stats on the instance.
        """
        instance = URLMapping.objects.get_or_none(short_code=code, is_active=True)
        if not instance:
            raise ValidationError("Instance not found.")

        if fetch:
            instance.update_stats()
            instance.save()
        return instance

    @staticmethod
    @transaction.atomic
    def create(data: dict):
        """Create a new URL mapping."""
        serializer = URLShortenCUDSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            return serializer.save()
        raise ValidationError("Instance not found.")

    @staticmethod
    @transaction.atomic
    def update(code: str, data: dict):
        """Partially update an existing URL mapping."""
        instance = URLShortenService.get(code)
        serializer = URLShortenCUDSerializer(instance, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            return serializer.save()
        raise ValidationError("Instance not found.")

    @staticmethod
    def delete(code: str):
        """Deactivate a URL mapping (soft delete)."""
        instance = URLShortenService.get(code)
        instance.delete()
