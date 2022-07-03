from django.urls import path

from . import views

urlpatterns = [

    path("reviews/", views.ReviewView.as_view()),
    path("movies/<int:movie_id>/reviews/", views.ReviewDetail.as_view()),
    path("reviews/<int:review_id>/", views.ReviewViewDelete.as_view())
]