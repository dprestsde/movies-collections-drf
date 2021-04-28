from rest_framework.views import APIView
from movies.utils import get_movies_data
from rest_framework.response import Response
from movies.models import Collection
from movies.serializers import CollectionSerializer, CollectionDetailSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from collections import Counter, OrderedDict
from django.contrib.admin.utils import flatten
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class MoviesListView(APIView):
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """ Use to return movies list """
        page = request.GET.get("page", 1)
        data = get_movies_data(page=page)
        return Response(data)


class CollectionView(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        collection = self.perform_create(serializer)
        response = {"collection_uuid": collection.uuid}
        headers = self.get_success_headers(serializer.data)
        return Response(
            response,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def list(self, request, *args, **kwargs):
        response = {}
        res_status = None
        try:
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
            genre_freq = Counter(
                flatten(
                    [
                        j.genre_list
                        for i in Collection.objects.all()
                        for j in i.movies_list
                    ]
                )
            )
            favourite_genres = ", ".join(
                list(
                    OrderedDict(
                        sorted(genre_freq.items(),
                               key=lambda kv: kv[1], reverse=True)
                    )
                )[:3]
            )
            response["is_success"] = True
            res_status = status.HTTP_200_OK
            response["collection"] = serializer.data
            response["favourite_genres"] = favourite_genres
        except Exception:
            response["is_success"] = False
            res_status = status.HTTP_400_BAD_REQUEST
        return Response(response, status=res_status)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = CollectionDetailSerializer(instance)
        return Response(serializer.data)
