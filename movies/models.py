from django.db import models
import uuid
from collections import Counter, OrderedDict
from django.contrib.admin.utils import flatten
from django.contrib.auth.models import User


class Movies(models.Model):
    uuid = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    genres = models.CharField(max_length=512)

    @property
    def genre_list(self):
        return self.genres.split(",")


class Collection(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=1024)
    movies = models.ManyToManyField(Movies, blank=True)

    @property
    def movies_list(self):
        return self.movies.all()

    @property
    def movies_genre_freq(self):
        genre_freq = Counter(flatten([i.genre_list for i in self.movies_list]))
        ordered_freq = OrderedDict(
            sorted(genre_freq.items(), key=lambda kv: kv[1], reverse=True)
        )
        return ordered_freq
