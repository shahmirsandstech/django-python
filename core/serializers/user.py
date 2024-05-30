from rest_framework import serializers
from django.contrib.auth.models import User
from home.models import UserDetailModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email','username']
        
        
class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetailModel
        fields = '__all__'
        