from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Review
from users.models import User
from .serializers import ReviewSerializer
from rest_framework.exceptions import ParseError, NotFound

class UserNameReview(APIView):
  def get(self,request,username):
    try:
      user= User.objects.get(username=username)
      
      user_review = Review.objects.filter(author=user)
    except Review.DoesNotExist:
      raise NotFound
    serializer = ReviewSerializer(user_review, many=True)
    return Response(serializer.data)