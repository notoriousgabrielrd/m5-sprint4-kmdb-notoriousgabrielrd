from pydoc import synopsis
from rest_framework import serializers
from genres.models import Genre
from genres.serializer import GenreSerializer
from movies.models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    premiere = serializers.DateField()
    classification = serializers.CharField(max_length=20)
    synopsis = serializers.CharField(max_length=255)

    genres = GenreSerializer(many=True)
    # review = Review

        
    def create(self, validated_data:dict):
        valid_genre = validated_data.pop("genres")

        movie = Movie.objects.create(**validated_data)
        
        for item in valid_genre:

            new_genre,_ = Genre.objects.get_or_create(**item)
        
            movie.genres.add(new_genre)

        return movie


    def update(self, instance: Movie, validated_data:dict):

        for key, value in validated_data.items():
            setattr(instance,key,value)

        instance.save()

        return instance