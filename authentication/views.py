from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

from authentication.serializers import UserSerializer, VisitorCountSerializer
from authentication.models import VisitorCount
from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class VisitorCountView(APIView):
    authentication_classes = [
        TokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        q_obj = VisitorCount.objects.first()
        serializer = VisitorCountSerializer(q_obj)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        res_status = None
        try:
            q_obj = VisitorCount.objects.first()
            q_obj.reset()
            msg = "request count reset successfully"
            res_status = status.HTTP_200_OK
        except Exception:
            msg = "request count reset failed"
            res_status = status.HTTP_400_BAD_REQUEST
        return Response({"message": msg}, status=res_status)
