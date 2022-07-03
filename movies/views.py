from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Movie
from .serializer import MovieSerializer

from .permissions import MyCustomPermission
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination

class MovieView(APIView,PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermission]


    def post(self,request):

        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def get(self,request):
        movies = Movie.objects.all()

        result_page = self.paginate_queryset(movies,request,view=self)

        serializer = MovieSerializer(result_page, many=True)

        # return Response(serializer.data)
        return self.get_paginated_response(serializer.data)


class MovieViewDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermission]


    def get(self,request,movie_id):

        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response(
                {"message": "Movie not found."},
                status.HTTP_404_NOT_FOUND
            )
        serializer = MovieSerializer(movie)

        return Response(serializer.data)
    

    def patch(self,request,movie_id):
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({"message": "This movie was not found!"}, status.HTTP_404_NOT_FOUND)

        serializer = MovieSerializer(movie, request.data, partial=True)

        serializer.is_valid()

        serializer.save()

        return Response(serializer.data)

    def delete(self,request, movie_id):

        try:
            movie = Movie.objects.get(pk=movie_id)

            movie.delete()

            return Response(status = status.HTTP_204_NO_CONTENT)

        except Movie.DoesNotExist:

            return Response({"Message": "This movie was not found!"}, status.HTTP_404_NOT_FOUND)
