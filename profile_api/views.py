from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profile_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

#always use SELF in a function
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP method as a function (get, post, patch, put, delete)'
            'Is similar to a traditional Django View'
            'Gives you the most control over your application logic'
            'Is mapped manually to URLs'
        ]
        #used to return an objects

        return Response({'message': 'Hello!','an_apiview':an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            surname = serializer.validated_data.get('surname')
            age = serializer.validated_data.get('age')
            nationality = serializer.validated_data.get('nationality')
            idbirth = serializer.validated_data.get('idbirth')
            message = f'Hello {name}  {surname} {age}'

            return Response({'message': message})

        else:
            return Response(
            serializer.errors,
            status = status.HTTP_400_BAD_REQUEST
             )

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'Put'})

    def patch(self, request, pk=None):
        """Handle a partial update of an object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'DELETE'})
