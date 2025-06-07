from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from common.models import URLMapping
from services import URLShortenService
from shorten.serializers import URLShortenRetrieveSerializer, URLShortenStatsSerializer


class URLShortenStatsViewSet(viewsets.ReadOnlyModelViewSet):
    """View to retrieve stats of respective URLMapping instance."""

    queryset = URLMapping.objects.filter(is_active=True)
    serializer_class = URLShortenStatsSerializer
    lookup_field = "short_code"



class URLShortenCRUDViewSet(viewsets.ViewSet):
    """CRUD view for URLMapping instance."""

    def create(self, request):
        """Create a new shortened URL entry."""
        instance = URLShortenService.create(data=request.data)
        serializer = URLShortenRetrieveSerializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, short_code=None):
        """Retrieve an active URL mapping and optionally update access statistics."""
        instance = URLShortenService.get(code=short_code, fetch=True)
        serializer = URLShortenRetrieveSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, short_code=None):
        """Partially update an existing URL mapping using its short code."""
        instance = URLShortenService.update(code=short_code, data=request.data)
        serializer = URLShortenRetrieveSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, short_code=None):
        """Deactivate (or delete) a URL mapping by short code."""
        URLShortenService.delete(short_code)
        return Response(status=status.HTTP_204_NO_CONTENT)


    @action(detail=True, methods=["get"], url_path="stats")
    def stats(self, request, short_code=None):
        """Retrieve stats of respective URLMapping instance."""
        instance = URLShortenService.get(code=short_code, fetch=True)
        serializer = URLShortenStatsSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
