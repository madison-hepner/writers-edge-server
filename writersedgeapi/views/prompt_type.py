"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from writersedgeapi.models import Prompt_Type


class PromptTypeView(ViewSet):

    def retrieve(self, request, pk):
        prompt_types = Prompt_Type.objects.get(pk=pk)
        serializer = PromptTypeSerializer(prompt_types)
        return Response(serializer.data)

    def list(self, request):
        prompt_types = Prompt_Type.objects.all()
        serializer = PromptTypeSerializer(prompt_types, many=True)
        return Response(serializer.data)


class PromptTypeSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Prompt_Type
        fields = ('id', 'prompt_type')