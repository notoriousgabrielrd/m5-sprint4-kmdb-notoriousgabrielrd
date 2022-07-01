from rest_framework import serializers
from accounts.models import User

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    email = serializers.EmailField(max_length = 255)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    updated_at = serializers.DateTimeField(read_only = True)
    date_joined = serializers.DateTimeField(read_only=True)
    password = serializers.CharField(write_only=True)

    def validate_email(self,value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email já existe.")

        return value

    def create(self, validated_data:dict)-> User:
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(write_only=True)
