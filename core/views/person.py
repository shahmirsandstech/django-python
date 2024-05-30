from rest_framework.views import APIView
from rest_framework.response import Response
from home.models import PersonModel
from serializers.person import PersonSerializer


class PersonView(APIView):
    def get(self, request, format=None):
        objs = PersonModel.objects.all()
        serializer = PersonSerializer(objs, many=True)
        if serializer.is_valid:
            return Response(serializer.data)
        else:
            return Response(serializer.errors)