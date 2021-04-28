from rest_framework.serializers import ModelSerializer
from movies.models import Movies, Collection


class MoviesSerializer(ModelSerializer):
    class Meta:
        model = Movies
        fields = "__all__"


class CollectionSerializer(ModelSerializer):
    def save(self, **kwargs):
        movies_data = self.context["request"].data.get("movies", None)
        movie_objects = []
        if movies_data:
            for movie_data in movies_data:
                movie_serializer = MoviesSerializer(data=movie_data)
                if movie_serializer.is_valid():
                    movie_objects.append(movie_serializer.save())
                else:
                    movie = Movies.objects.filter(
                        uuid=movie_serializer.data["uuid"]
                    )
                    if movie.first():
                        movie = movie.first()
                        movie.title = movie_serializer.data["title"]
                        movie.description = movie_serializer\
                            .data["description"]
                        movie.genres = movie_serializer.data["genres"]
                        movie.save()
                        movie_objects.append(movie)
        collection = None
        self.validated_data["user"] = self.context["request"].user
        if self.instance is not None:
            self.instance = self.update(self.instance, self.validated_data)
            collection = self.instance
        else:
            collection = self.create(self.validated_data)
            self.instance = collection
        if movies_data is not None:
            curr_movies = collection.movies.all()
            for obj in curr_movies:
                collection.movies.remove(obj)
            for movie in movie_objects:
                collection.movies.add(movie)
        return collection

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["uuid"] = instance.uuid
        return data

    class Meta:
        model = Collection
        fields = (
            "title",
            "description",
        )


class CollectionDetailSerializer(ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        movies = instance.movies.all()
        movie_data = MoviesSerializer(movies, many=True)
        data["movies"] = movie_data.data
        return data

    class Meta:
        model = Collection
        fields = (
            "title",
            "description",
        )
