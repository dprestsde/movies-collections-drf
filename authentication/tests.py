from django.test import TestCase, Client
from authentication.models import VisitorCount
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token

client = Client()


class VisitorCountTest(TestCase):
    """Test module for Visitor Count model"""

    def test_count_increment(self):
        visits = VisitorCount.objects.create()
        visits = visits.increment()
        visits = visits.increment()
        self.assertEqual(visits.count, 2)

    def test_count_reset(self):
        visits = VisitorCount.objects.create()
        visits = visits.increment()
        visits = visits.increment()
        visits = visits.reset()
        self.assertEqual(visits.count, 0)


class UserTest(TestCase):
    """Testing user model"""

    def setUp(self):
        user = User.objects.create(username="Test username")
        user.set_password("bd6528b0wns$$ybsk")

    def test_user(self):
        user = User.objects.get(username="Test username")
        self.assertEqual(user.username, "Test username")


class AuthTests(TestCase):
    """Tests for authentication APIs for registration, login"""

    def setUp(self):
        user = User.objects.create(username="johndoe")
        user.set_password("john@credy")
        user.save()
        Token.objects.create(user=user)

    def test_registration(self):
        url = reverse("register")
        body = {"username": "testusername", "password": "bs62892dbjnjdbv"}
        response = client.post(url, data=body)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        user = User.objects.get(username="johndoe")
        token = Token.objects.get(user=user)
        url = reverse("login")
        body = {"username": "johndoe", "password": "john@credy"}
        response = client.post(url, data=body)
        self.assertEqual(response.data["token"], token.key)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class VisitorCountTests(TestCase):
    """Tests for authentication APIs for registration, login"""

    def setUp(self):
        _ = VisitorCount.objects.create()
        user = User.objects.create(username="johndoe")
        user.set_password("john@credy")
        user.save()
        _ = Token.objects.create(user=user)

    def test_visitor_increments(self):
        user = User.objects.get(username="johndoe")
        token = Token.objects.get(user=user)
        token = token.key
        url = reverse("visitor-count")
        before_req = VisitorCount.objects.first()
        _ = client.get(url, HTTP_AUTHORIZATION="Token {}".format(token))
        after_req = VisitorCount.objects.first()
        self.assertEqual(before_req.count + 1, after_req.count)

    def test_visitor_count(self):
        user = User.objects.get(username="johndoe")
        token = Token.objects.get(user=user)
        token = token.key
        url = reverse("visitor-count")
        response = client.get(url, HTTP_AUTHORIZATION="Token {}".format(token))
        curr_count = VisitorCount.objects.first()
        self.assertEqual(curr_count.count, response.data["count"])

    def test_visitor_reset(self):
        user = User.objects.get(username="johndoe")
        token = Token.objects.get(user=user)
        token = token.key
        url = reverse("visitor-count-reset")
        response = client.post(
            url,
            HTTP_AUTHORIZATION="Token {}".format(token)
        )
        curr_count = VisitorCount.objects.first()
        self.assertEqual(curr_count.count, 0)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
