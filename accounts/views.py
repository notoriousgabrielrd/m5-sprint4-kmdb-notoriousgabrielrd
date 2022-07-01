from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.views import APIView, Response, status
from rest_framework.authtoken.models import Token
from accounts.models import User

from accounts.serializer import LoginSerializer, UserSerializer

class RegisterView(APIView):
    
    def post(self,request):
        
        serializer = UserSerializer(data = request.data)

        serializer.is_valid(raise_exception=True)

        # user = User.objects.create_user(**serializer.validated_data)

        # serializer = UserSerializer(user)

        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)
        

class LoginView(APIView):

    def post(self,request):

        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = authenticate(
            username = serializer.validated_data["email"],
            password = serializer.validated_data["password"]
            )

        if user:
            token, _ = Token.objects.get_or_create(user=user)
            # token = Tken.objects.get_or_create(user=user)[0]

            return Response({"token": token.key})

        return Response(
            {"detail": "Invalid email or password, i can't say..."}, status.HTTP_401_UNAUTHORIZED
        )