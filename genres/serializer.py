from rest_framework import serializers
from movies.models import Movie

class GenreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=127)