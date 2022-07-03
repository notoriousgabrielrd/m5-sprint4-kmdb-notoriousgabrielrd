from django.shortcuts import get_object_or_404, render
import ipdb
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from movies.models import Movie
from reviews.utils import review_util
from .models import Review
from .serializer import ReviewSerializer

from .permissions import IsOwner, MyCustomPermission
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination


class ReviewView(APIView,PageNumberPagination):

    
    def get(self,request):

        reviews = Review.objects.all()

        result_page = self.paginate_queryset(reviews,request, view = self)

        serializer = ReviewSerializer(result_page, many=True)

        for item in serializer.data:
            review_util(item)

        
        return self.get_paginated_response(serializer.data)

class ReviewDetail(APIView,PageNumberPagination):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermission]

    def post(self,request,movie_id):

        
        movie = get_object_or_404(Movie,id = movie_id )


        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
  

        serializer.save(movie = movie, critic = request.user)


        return Response(review_util(serializer.data))



    def get(self,request,movie_id): 

       
        review = Review.objects.filter(movie_id=movie_id)
            
        if len(review) == 0:
            return Response({"message": "movie not found"})
       

        result_page = self.paginate_queryset(review,request,view=self)

        serializer = ReviewSerializer(result_page, many = True)

        for item in serializer.data:
            review_util(item)

        return self.get_paginated_response(serializer.data)




class ReviewViewDelete(APIView):
    authentication_classes = [TokenAuthentication]  # diz que tipo sera
    permission_classes = [IsOwner] ##diz que vai ter verificaçãp

    def delete(self,request,review_id):
        review = get_object_or_404(Review,id = review_id )
        self.check_object_permissions(request,review)

    
        review.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)