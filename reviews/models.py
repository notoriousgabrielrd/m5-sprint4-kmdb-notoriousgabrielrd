from sys import maxsize
from django.db import models

# Create your models here.



class CategoryReview(models.TextChoices):
    MUST_WATCH = ("Must watch")
    SHOULD_WATCH = ("Should watch")
    AVOID_WATCH = ("Avoid watch")
    NO_OPINION = ("No opinion")

class Review(models.Model):
 
    stars = models.IntegerField()
    review = models.TextField()
    spoilers = models.BooleanField(default=False)
    recomendation = models.CharField(max_length=50, choices=CategoryReview.choices, default=CategoryReview.NO_OPINION)


    movie = models.ForeignKey("movies.Movie",on_delete=models.CASCADE, related_name="reviews")

    critic = models.ForeignKey("accounts.User",on_delete=models.CASCADE,related_name="reviews")



