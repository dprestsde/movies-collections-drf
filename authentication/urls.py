from django.urls import path
from authentication.views import CreateUserView
from rest_framework.authtoken import views
from authentication.views import VisitorCountView

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="register"),
    path("token/", views.obtain_auth_token, name="login"),
    path("request-count/", VisitorCountView.as_view(), name="visitor-count"),
    path(
        "request-count/reset/", VisitorCountView.as_view(),
        name="visitor-count-reset"
    ),
]
