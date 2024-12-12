from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializers
from rest_framework import status                #error cpde to returm
from rest_framework import viewsets


# Create your views here.
class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloWordSerializers

    def get(self, request, format=None):
        """return list of API bview feature"""

        an_apiview = [
        'use http method an a function( get, post,delete, put, patchh)',
        'is more similar to traditional django view',
        'gives more control over your application logic',
        'is manually map to URL'
        ]

        return Response({'messages': "Hello", 'an_apiview': an_apiview})

    def post(self, request):
        """create hello message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """handle updating an objects"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """handle a partial update an object"""
        return Response({'method': "PATCH"})

    def delete(self, request, pk=None):
        """handled delete an object"""
        return Response({'method': 'DELETE'})


#
# class HelloViewSet(viewsets.ViewSet):
#     """Test API ViewSet"""
#
#     def list(self, request):
#         """return hello messgae"""
#         a_viewset = [
#         "Uses action (list, update, partial update, create retrive)",
#         "Autoamyically map URL using router",
#         "provide more functionallity with less code"
#         ]
#         return Response({'message': 'Hello', 'a_viewset': a_viewset})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloWordSerializers

    def list(self, request):
        """Return a hello message"""
        a_viewset = [
            'Uses actions (list, create,retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello Message"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name}'
            return Response({'message': message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """handle getting new object by IDs"""
        return Response({'http_method': 'GET'})
    #
    # def update(self, request, pk=None):
    #     """handle updating an object"""
    #     return Response({'http_method': 'PUT'})
    #
    # def partial_update(self,  request, pk=None):
    #     """handle partial updating an object"""
    #     return Response({'http_method': 'PATCH'})
    #
    # def destroy(self, request, pk=None):
    #     """handle deleting an object"""
    #     return Response({'http_method': 'DELETE'})


    # def retrieve(self, request, pk=None):
    #     """Handle getting an object by its ID"""
    #     return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""
        return Response({'http_method': 'DELETE'})
