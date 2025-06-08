from drf_spectacular.utils import extend_schema
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from services import URLShortenService
from shorten.serializers import (
    URLShortenCUDSerializer,
    URLShortenRetrieveSerializer,
    URLShortenStatsSerializer,
)


class URLShortenCRUDViewSet(viewsets.ViewSet):
    """CRUD view for URLMapping instance."""

    @extend_schema(
        request=URLShortenCUDSerializer,
        responses=URLShortenRetrieveSerializer,
        description="Creates URLMapping instance."
    )
    def create(self, request):
        """Create a new shortened URL entry."""
        instance = URLShortenService.create(data=request.data)
        serializer = URLShortenRetrieveSerializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    @extend_schema(
        responses=URLShortenRetrieveSerializer,
        description="Retrieve respective URLMapping instance by short code."
    )
    def retrieve(self, request, short_code=None):
        """Retrieve an active URL mapping and optionally update access statistics."""
        instance = URLShortenService.get(code=short_code, fetch=True)
        serializer = URLShortenRetrieveSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @extend_schema(
        request=URLShortenCUDSerializer,
        responses=URLShortenRetrieveSerializer,
        description="Updates respective URLMapping instance by short code."
    )
    def update(self, request, short_code=None):
        """Partially update an existing URL mapping using its short code."""
        instance = URLShortenService.update(code=short_code, data=request.data)
        serializer = URLShortenRetrieveSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @extend_schema(
        description="Deletes respective URLMapping instance by short code."
    )
    def destroy(self, request, short_code=None):
        """Deactivate (or delete) a URL mapping by short code."""
        URLShortenService.delete(short_code)
        return Response(status=status.HTTP_204_NO_CONTENT)


    @extend_schema(
        description="Retrieve stats of the respective URLMapping instance by short code.",
        responses=URLShortenRetrieveSerializer,
    )
    @action(detail=True, methods=["get"], url_path="stats")
    def stats(self, request, short_code=None):
        """Retrieve stats of respective URLMapping instance."""
        instance = URLShortenService.get(code=short_code, fetch=True)
        serializer = URLShortenStatsSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
