from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Movie
from .serializer import MovieSerializer

class MovieView(APIView):

    def post(self,request):

        serializer = MovieSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def get(self,request):
        movies = Movie.objects.all()

        serializer = MovieSerializer(movies, many=True)

        return Response(serializer.data)


class MovieViewDetail(APIView):
    
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
    