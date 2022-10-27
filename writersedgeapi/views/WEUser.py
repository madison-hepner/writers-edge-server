"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from writersedgeapi.models import WEUser


class UserView(ViewSet):

    def retrieve(self, request, pk):
        weusers = WEUser.objects.get(pk=pk)
        serializer = UserSerializer(weusers)
        return Response(serializer.data)

    def list(self, request):
        weusers = WEUser.objects.all()
        serializer = UserSerializer(weusers, many=True)
        return Response(serializer.data)
    
    


class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = WEUser
        fields = ('id', 'user')
