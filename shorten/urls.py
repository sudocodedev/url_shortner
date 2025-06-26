from django.urls import path

from shorten.views import URLShortenCRUDViewSet

app_name = "shorten"

# only for create operation
url_shorten_create = URLShortenCRUDViewSet.as_view({"post": "create"})

# only for retrieve, update & delete operation
url_shorten_RUD = URLShortenCRUDViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})


API_URL_PREFIX = "shorten"

urlpatterns = [
    path(f"{API_URL_PREFIX}/", url_shorten_create),
    path(f"{API_URL_PREFIX}/<str:short_code>/", url_shorten_RUD),
    path(f"{API_URL_PREFIX}/<str:short_code>/stats/", URLShortenCRUDViewSet.as_view({"get": "stats"})),
]
