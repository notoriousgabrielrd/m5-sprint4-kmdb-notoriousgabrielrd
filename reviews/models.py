from django.db import models

# Create your models here.


class Review(models.Model):
    start = models.IntegerField()
    review = models.TextField()
    spoiler = models.BooleanField(False)
    recomendation = models.CharField(max_length=50)


    movie = models.ForeignKey("movies.Movie",on_delete=models.CASCADE, related_name="reviews")

    user = models.ForeignKey("accounts.User",on_delete=models.CASCADE,related_name="reviews")