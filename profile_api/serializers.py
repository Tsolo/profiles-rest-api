from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)
    surname = serializers.CharField(max_length=10)
    age = serializers.CharField(max_length=10)
    nationality = serializers.CharField(max_length=10)
    idbirth = serializers.CharField(max_length=10)
