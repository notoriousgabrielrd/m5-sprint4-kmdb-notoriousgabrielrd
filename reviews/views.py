from django.shortcuts import get_object_or_404, render
import ipdb
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from traitlets import validate
from accounts.serializer import UserSerializer

from movies.models import Movie
from movies.serializer import MovieSerializer
from reviews.utils import review_util
from .models import Review
from .serializer import ReviewSerializer

from .permissions import IsOwner, MyCustomPermission
from rest_framework.authentication import TokenAuthentication


class ReviewView(APIView):

    
    def get(self,request):

        reviews = Review.objects.all()

        serializer = ReviewSerializer(reviews, many=True)

        for item in serializer.data:
            review_util(item)

        
        return Response(serializer.data)

class ReviewDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [MyCustomPermission]

    def post(self,request,movie_id):

        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return({
                {"Message":"Movie not found."},status.HTTP_404_NOT_FOUND
            })
        # print(">>>>>>>>>>>>>>>>",request.user.id)
   
        user_serial = UserSerializer(data=request.user)
        # movie_serial = MovieSerializer(data=request.user)


        # request.data["critic_id"] = request.user
        # request.data["movie"] = movie
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
  


        # import ipdb
        # ipdb.set_trace()
        # serializer.save()



        serializer.save(movie = movie, critic = request.user)


        # serializer.save(movie = movie, critic = request.user


        return Response(review_util(serializer.data))



    def get(self,request,movie_id): 

       
        review = Review.objects.filter(movie_id=movie_id)
            
        # ipdb.set_trace()

        print(review)
        if len(review) == 0:
            return Response({"message": "movie not found"})
       
        serializer = ReviewSerializer(review, many = True)

        for item in serializer.data:
            review_util(item)

        return Response(serializer.data)



        # isntance -> obj.py pronto -> obj.json
        # data = obj.json para obj.py



class ReviewViewDelete(APIView):
    authentication_classes = [TokenAuthentication]  # diz que tipo sera
    permission_classes = [IsOwner] ##diz que vai ter verificaçãp

    def delete(self,request,review_id):
        review = get_object_or_404(Review,id = review_id )
        self.check_object_permissions(request,review)

    
        review.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)