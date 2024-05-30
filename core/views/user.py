from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from serializers.user import UserSerializer


class UserRegistrationView(APIView):
    def get(self, request, format=None):
        objs = User.objects.all()
        serializer = UserSerializer(objs, many=True)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("A new user registered",  status=201)
        else:
            return Response(serializer.errors)
        