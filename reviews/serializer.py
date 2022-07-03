from rest_framework import serializers

from .models import Review

from movies.serializer import MovieSerializer
from accounts.serializer import UserSerializer
class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        # fields = "__all__"
        fields = ["id","review", "spoilers","movie_id","recomendation","stars","critic"]
        extra_kwargs = {'stars':{'max_value':10,"min_value":1}}
        depth = 1

      