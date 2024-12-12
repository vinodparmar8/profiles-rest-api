from rest_framework import serializers

class HelloWordSerializers(serializers.Serializer):
    """Serializer name filed for testing API View"""
    name = serializers.CharField(max_length=10) 
