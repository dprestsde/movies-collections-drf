from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from authentication.models import VisitorCount

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create(
            username=validated_data["username"],
            password=validated_data["password"],
        )
        Token.objects.create(user=user)
        return user

    def to_representation(self, instance):
        token = Token.objects.get(user=instance)
        data = {"access_token": token.key}
        return data

    class Meta:
        model = UserModel
        fields = (
            "id",
            "username",
            "password",
        )


class VisitorCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = VisitorCount
        fields = ("count",)
