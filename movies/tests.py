from django.test import TestCase, Client
from movies.models import Movies, Collection
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from movies.data import (
    INVALID_TITLE_COLLECTION_SAMPLE_DATA,
    VALID_COLLECTION_SAMPLE_DATA,
    INVALID_DESC_COLLECTION_SAMPLE_DATA,
    UPDATED_COLLECTION_SAMPLE_DATA,
    UPDATED_EMPTY_MOVIES_SAMPLE_DATA,
    UPDATED_TITLE_MOVIES_SAMPLE_DATA,
    UPDATED_DESC_MOVIES_SAMPLE_DATA,
)

import json


client = Client()


class MoviesTest(TestCase):
    """Test module for Movies model"""

    def setUp(self):
        Movies.objects.create(
            uuid="a2f0e3a8-f505-4372-a52f-0b91aa87c9b0",
            title="John Wick",
            description="He is portrayed by Keanu Reeves. \
                John Wick is a legendary hitman who retired \
                    until a gang invades his house, steals \
                        his car, and kills the puppy his late\
                             wife Helen had given him.",
            genres="Action,Crime,thriller",
        )
        Movies.objects.create(
            uuid="e63c7840-fbfd-44f8-9a71-47847bcf84e9",
            title="Predestination",
            description="As his last assignment, a temporal agent\
                 is tasked to travel back in time and prevent a \
                     bomb attack in New York in 1975. The hunt, \
                         however, turns out to be beyond the \
                             bounds of possibility.",
            genres="Action, Sci-Fi",
        )

    def test_movies(self):
        john_wick = Movies.objects.get(
            uuid="a2f0e3a8-f505-4372-a52f-0b91aa87c9b0")
        pre_destination = Movies.objects.get(
            uuid="e63c7840-fbfd-44f8-9a71-47847bcf84e9"
        )
        self.assertEqual(john_wick.title, "John Wick")
        self.assertEqual(pre_destination.title, "Predestination")


class CollectionTest(TestCase):
    """Test module for Collection model"""

    def setUp(self):
        movie1 = Movies.objects.create(
            uuid="a2f0e3a8-f505-4372-a52f-0b91aa87c9b0",
            title="John Wick",
            description="He is portrayed by Keanu Reeves. \
                John Wick is a legendary hitman who retired \
                    until a gang invades his house, steals \
                        his car, and kills the puppy his \
                            late wife Helen had given him.",
            genres="Action,Crime,thriller",
        )
        movie2 = Movies.objects.create(
            uuid="e63c7840-fbfd-44f8-9a71-47847bcf84e9",
            title="Predestination",
            description="As his last assignment, a temporal agent\
                 is tasked to travel back in time and prevent a \
                     bomb attack in New York in 1975. The hunt, \
                         however, turns out to be beyond the bounds \
                             of possibility.",
            genres="Action, Sci-Fi",
        )
        user = User.objects.create(username="Deepak")
        user.set_password("dyb387bddwyue")
        collection = Collection.objects.create(
            uuid="0f8b4ec5-6c34-45c9-9c3a-f2d2c89911ef",
            user=user,
            title="Action Movies",
            description="My favourite action movies",
        )
        collection2 = Collection.objects.create(
            uuid="92a1fbc4-f481-4346-846a-c189f1e4904e",
            user=user,
            title="Action Movies second collection",
            description="My favourite action movies (second collection)",
        )
        collection.movies.add(movie1)
        collection.movies.add(movie2)
        collection2.movies.add(movie1)

    def test_collection(self):
        collection = Collection.objects.get(
            uuid="0f8b4ec5-6c34-45c9-9c3a-f2d2c89911ef")
        self.assertEqual(collection.title, "Action Movies")
        self.assertEqual(collection.movies.all().count(), 2)

    def test_collection2(self):
        collection = Collection.objects.get(
            uuid="92a1fbc4-f481-4346-846a-c189f1e4904e")
        self.assertEqual(collection.title, "Action Movies second collection")
        self.assertEqual(collection.movies.all().count(), 1)


class AuthTestCase(TestCase):
    """
    Parent Class to generate a user and
    associate token to authorize a request
    """

    def setUp(self):
        user = User.objects.create(username="johndoe")
        user.set_password("john@credy")
        user.save()
        token = Token.objects.create(user=user)
        self.token = token


class MoviesListAPITests(AuthTestCase):
    """Use to test list movies API"""

    def test_movies_list(self):
        url = reverse("movies-list")
        response = client.get(
            url, HTTP_AUTHORIZATION="Token {}".format(self.token))

        self.assertEqual(response.data["count"], 45466)
        self.assertEqual(len(response.data["results"]), 10)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CollectionCreationTests(AuthTestCase):
    """Tests for Collection data generation APIs"""

    def test_valid_collection_creation(self):
        """
        testing behaviour of Create Collection
        API when a valid data is passed
        """
        url = reverse("collection-urls")
        data = json.dumps(VALID_COLLECTION_SAMPLE_DATA)
        response = client.post(
            url,
            data=data,
            content_type="application/json",
            HTTP_AUTHORIZATION="Token {}".format(self.token),
        )
        collection_uuid = response.data["collection_uuid"]
        collection = Collection.objects.get(uuid=collection_uuid)
        self.assertEqual(collection.title,
                         VALID_COLLECTION_SAMPLE_DATA["title"])
        self.assertEqual(
            collection.description, VALID_COLLECTION_SAMPLE_DATA["description"]
        )
        self.assertEqual(
            collection.movies.all().count(), len(
                VALID_COLLECTION_SAMPLE_DATA["movies"])
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_title_collection_creation(self):
        """
        testing behaviour of Create Collection API when a
        data with invalid title is passed
        """
        url = reverse("collection-urls")
        data = json.dumps(INVALID_TITLE_COLLECTION_SAMPLE_DATA)
        response = client.post(
            url,
            data=data,
            content_type="application/json",
            HTTP_AUTHORIZATION="Token {}".format(self.token),
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_description_collection_creation(self):
        """
        testing behaviour of Create Collection API when a data with invalid
        description is passed
        """
        url = reverse("collection-urls")
        data = json.dumps(INVALID_DESC_COLLECTION_SAMPLE_DATA)
        response = client.post(
            url,
            data=data,
            content_type="application/json",
            HTTP_AUTHORIZATION="Token {}".format(self.token),
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class CollectionRetrievalTests(AuthTestCase):
    """Tests for collection retrieval(detail and list) APIs"""

    def create_collection_data(self):
        """Reusable method to generate collection data"""
        url = reverse("collection-urls")
        data = json.dumps(VALID_COLLECTION_SAMPLE_DATA)
        response = client.post(
            url,
            data=data,
            content_type="application/json",
            HTTP_AUTHORIZATION="Token {}".format(self.token),
        )
        return response

    def test_non_empty_collection_list_retrieval(self):
        """Testing the list collection api when there is data"""
        _ = self.create_collection_data()
        _ = self.create_collection_data()
        _ = self.create_collection_data()
        url = reverse("collection-urls")
        collection_response = client.get(
            url, HTTP_AUTHORIZATION="Token {}".format(self.token),
        )
        collection_list = collection_response.data
        collection_count = Collection.objects.all().count()
        self.assertEqual(len(collection_list["collection"]), collection_count)
        self.assertEqual(collection_response.status_code, status.HTTP_200_OK)

    def test_empty_valid_collection_list_retrieval(self):
        """Testing the list collection api when there is no data"""
        url = reverse("collection-urls")
        collection_response = client.get(
            url, HTTP_AUTHORIZATION="Token {}".format(self.token),
        )
        collection_list = collection_response.data
        self.assertEqual(len(collection_list["collection"]), 0)
        self.assertEqual(collection_response.status_code, status.HTTP_200_OK)

    def test_valid_collection_detail_retrieval(self):
        """
        testing API to retrieval a particular collection
        object which is present in DB
        """
        response = self.create_collection_data()
        collection_uuid = response.data["collection_uuid"]
        url = reverse("collection-detail-urls", kwargs={"pk": collection_uuid})
        collection = Collection.objects.get(uuid=collection_uuid)
        collection_response = client.get(
            url, HTTP_AUTHORIZATION="Token {}".format(self.token),
        )
        self.assertEqual(collection.title, collection_response.data["title"])
        self.assertEqual(
            collection.description, collection_response.data["description"]
        )
        self.assertEqual(
            collection.movies.all().count(), len(
                collection_response.data["movies"])
        )
        self.assertEqual(collection_response.status_code, status.HTTP_200_OK)

    def test_invalid_collection_detail_retrieval(self):
        """
        testing API to retrieval a particular collection object which is
        not present in DB
        """
        url = reverse(
            "collection-detail-urls",
            kwargs={"pk": "0c9fbffb-4bfd-4546-8eea-50ed08f74a6d"},
        )
        collection_response = client.get(
            url, HTTP_AUTHORIZATION="Token {}".format(self.token),
        )
        self.assertEqual(collection_response.status_code,
                         status.HTTP_404_NOT_FOUND)


class CollectionDeleteTests(AuthTestCase):
    """Tests for APIs to delete a collection object"""

    def test_existant_item_deletion(self):
        """
        Deleting a existing collection object
        """
        url = reverse("collection-urls")
        data = json.dumps(VALID_COLLECTION_SAMPLE_DATA)
        response = client.post(
            url,
            data=data,
            content_type="application/json",
            HTTP_AUTHORIZATION="Token {}".format(self.token),
        )
        collection_uuid = response.data["collection_uuid"]
        url = reverse("collection-detail-urls", kwargs={"pk": collection_uuid})

        collection_response = client.delete(
            url, HTTP_AUTHORIZATION="Token {}".format(self.token),
        )

        collection_obj = Collection.objects.filter(
            uuid=collection_uuid).first()
        self.assertEqual(collection_obj, None)
        self.assertEqual(collection_response.data, None)
        self.assertEqual(collection_response.status_code,
                         status.HTTP_204_NO_CONTENT)

    def test_non_existant_item_deletion(self):
        """Deleting a non existing collection object"""
        url = reverse(
            "collection-detail-urls",
            kwargs={"pk": "0c9fbffb-4bfd-4546-8eea-50ed08f74a6d"},
        )

        collection_response = client.delete(
            url, HTTP_AUTHORIZATION="Token {}".format(self.token),
        )
        self.assertEqual(collection_response.status_code,
                         status.HTTP_404_NOT_FOUND)


class UpdateCollectionAPITests(AuthTestCase):
    """Testing updation of collection APIs"""

    def create_collection_data(self):
        """Reusable method to geenrate sample data"""
        url = reverse("collection-urls")
        data = json.dumps(VALID_COLLECTION_SAMPLE_DATA)
        response = client.post(
            url,
            data=data,
            content_type="application/json",
            HTTP_AUTHORIZATION="Token {}".format(self.token),
        )
        return response

    def test_valid_updation(self):
        """tesing updation of collection object with valid updated data"""
        collection_response = self.create_collection_data()
        collection_uuid = collection_response.data["collection_uuid"]
        url = reverse("collection-detail-urls", kwargs={"pk": collection_uuid})
        data = json.dumps(UPDATED_COLLECTION_SAMPLE_DATA)
        collection_response = client.put(
            url,
            data=data,
            content_type="application/json",
            HTTP_AUTHORIZATION="Token {}".format(self.token),
        )

        collection_uuid = collection_response.data["uuid"]
        collection = Collection.objects.get(uuid=collection_uuid)
        self.assertEqual(collection.title,
                         UPDATED_COLLECTION_SAMPLE_DATA["title"])
        self.assertEqual(
            collection.description,
            UPDATED_COLLECTION_SAMPLE_DATA["description"]
        )
        self.assertEqual(
            collection.movies.all().count(),
            len(UPDATED_COLLECTION_SAMPLE_DATA["movies"]),
        )
        self.assertEqual(collection_response.status_code, status.HTTP_200_OK)

    def test_invalid_updation(self):
        """tesing updation of collection object with invalid updated data"""
        url = reverse(
            "collection-detail-urls",
            kwargs={"pk": "0c9fbffb-4bfd-4546-8eea-50ed08f74a6d"},
        )
        data = json.dumps(UPDATED_COLLECTION_SAMPLE_DATA)
        collection_response = client.put(
            url,
            data=data,
            content_type="application/json",
            HTTP_AUTHORIZATION="Token {}".format(self.token),
        )
        self.assertEqual(collection_response.status_code,
                         status.HTTP_404_NOT_FOUND)

    def test_clear_movies_updation(self):
        """
        testing the API if the user tries to delete movies from the collection
        """
        collection_response = self.create_collection_data()
        collection_uuid = collection_response.data["collection_uuid"]
        url = reverse("collection-detail-urls", kwargs={"pk": collection_uuid})
        data = json.dumps(UPDATED_EMPTY_MOVIES_SAMPLE_DATA)
        collection_response = client.put(
            url,
            data=data,
            content_type="application/json",
            HTTP_AUTHORIZATION="Token {}".format(self.token),
        )
        collection_uuid = collection_response.data["uuid"]
        collection = Collection.objects.get(uuid=collection_uuid)
        self.assertEqual(collection.title, collection_response.data["title"])
        self.assertEqual(
            collection.description, collection_response.data["description"]
        )
        self.assertEqual(
            collection.movies.all().count(), 0,
        )
        self.assertEqual(collection_response.status_code, status.HTTP_200_OK)

    def test_title_movies_updation(self):
        """Testing API if user tries to update ONLY title"""
        collection_response = self.create_collection_data()
        collection_uuid = collection_response.data["collection_uuid"]
        url = reverse("collection-detail-urls", kwargs={"pk": collection_uuid})
        data = json.dumps(UPDATED_TITLE_MOVIES_SAMPLE_DATA)
        collection_response = client.put(
            url,
            data=data,
            content_type="application/json",
            HTTP_AUTHORIZATION="Token {}".format(self.token),
        )
        collection_uuid = collection_response.data["uuid"]
        collection = Collection.objects.get(uuid=collection_uuid)
        self.assertEqual(
            collection_response.data["title"],
            UPDATED_TITLE_MOVIES_SAMPLE_DATA["title"]
        )
        self.assertEqual(collection_response.data["title"], collection.title)
        self.assertEqual(
            collection.description, collection_response.data["description"]
        )

        self.assertEqual(collection_response.status_code, status.HTTP_200_OK)

    def test_description_movies_updation(self):
        """Testing API if user tries to update ONLY description"""
        collection_response = self.create_collection_data()
        collection_uuid = collection_response.data["collection_uuid"]
        url = reverse("collection-detail-urls", kwargs={"pk": collection_uuid})
        data = json.dumps(UPDATED_DESC_MOVIES_SAMPLE_DATA)
        collection_response = client.put(
            url,
            data=data,
            content_type="application/json",
            HTTP_AUTHORIZATION="Token {}".format(self.token),
        )
        collection_uuid = collection_response.data["uuid"]
        collection = Collection.objects.get(uuid=collection_uuid)
        self.assertEqual(
            collection_response.data["description"],
            UPDATED_DESC_MOVIES_SAMPLE_DATA["description"],
        )
        self.assertEqual(
            collection_response.data["description"], collection.description
        )
        self.assertEqual(collection.title, collection_response.data["title"])

        self.assertEqual(collection_response.status_code, status.HTTP_200_OK)
