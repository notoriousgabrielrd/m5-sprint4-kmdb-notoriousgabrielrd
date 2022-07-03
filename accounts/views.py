from django.contrib.auth import authenticate
from rest_framework.views import APIView, Response, status
from rest_framework.authtoken.models import Token
from accounts.models import User

from accounts.serializer import LoginSerializer, UserSerializer

from .permissions import MyUserCustomPermission
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination

class RegisterView(APIView):
    
    def post(self,request):
        
        serializer = UserSerializer(data = request.data)

        serializer.is_valid(raise_exception=True)


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


class UserViewDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MyUserCustomPermission]



    def get(self,request, user_id):
        
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"Message": "This user was not found."}, status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)

        return Response(serializer.data)


class UserView(APIView,PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MyUserCustomPermission]

    def get(self,request):
        users = User.objects.all()

        result_page = self.paginate_queryset(users,request, view=self)

        serializer = UserSerializer(result_page,many=True)



        return self.get_paginated_response(serializer.data)
