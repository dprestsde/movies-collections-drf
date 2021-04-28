from django.urls import path
from movies.views import MoviesListView, CollectionView


urlpatterns = [
    path("list/", MoviesListView.as_view(), name="movies-list"),
    path(
        "collection/",
        CollectionView.as_view({"get": "list", "post": "create"}),
        name="collection-urls",
    ),
    path(
        "collection/<pk>/",
        CollectionView.as_view(
            {"get": "retrieve", "put": "partial_update", "delete": "destroy"}
        ),
        name="collection-detail-urls",
    ),
]
