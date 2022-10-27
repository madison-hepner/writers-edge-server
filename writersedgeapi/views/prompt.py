"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from writersedgeapi.models import Prompt


class PromptView(ViewSet):

    def retrieve(self, request, pk):
        prompts = Prompt.objects.get(pk=pk)
        serializer = PromptSerializer(prompts)
        return Response(serializer.data)

    def list(self, request):
        prompts = Prompt.objects.all()
        serializer = PromptSerializer(prompts, many=True)
        return Response(serializer.data)
    
    


class PromptSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Prompt
        fields = ('id', 'title', 'prompt_typeId')