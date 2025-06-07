from django.urls import path

from shorten.views import URLShortenCRUDViewSet

app_name = "shorten"

# only for create operation
url_shorten_create = URLShortenCRUDViewSet.as_view({"post": "create"})

# only for retrieve, update & delete operation
url_shorten_RUD = URLShortenCRUDViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})

urlpatterns = [
    path("shorten/", url_shorten_create),
    path("shorten/<str:short_code>/", url_shorten_RUD),
    path("shorten/<str:short_code>/stats/", URLShortenCRUDViewSet.as_view({"get": "retrieve"})),
]
