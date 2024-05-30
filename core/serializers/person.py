from rest_framework import serializers
from home.models import PersonModel

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonModel
        fields = '__all__'
            