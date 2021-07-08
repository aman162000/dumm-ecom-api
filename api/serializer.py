from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import exceptions
from .models import Product
from django.contrib.auth.models import User

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self,data):
        username = data.get("username","")
        password = data.get("password","")

        if username and password:
            user = authenticate(username = username, password= password)
            if user:
                data["user"] = user
            else:
                msg = "Invalid Credentials"
                raise exceptions.ValidationError(msg)
        else:

            msg = "Provide Username and Password"
            raise exceptions.ValidationError(msg)

        return data

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"