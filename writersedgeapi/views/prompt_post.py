"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from writersedgeapi.models import PromptPost, Prompt, Prompt_Type
from writersedgeapi.models.WEUser import WEUser


class PromptPostView(ViewSet):

    def retrieve(self, request, pk):
        prompt_posts = PromptPost.objects.get(pk=pk)
        serializer = PromptPostSerializer(prompt_posts)
        return Response(serializer.data)

    def list(self, request):
        prompt_posts = PromptPost.objects.all()
        serializer = PromptPostSerializer(prompt_posts, many=True)
        return Response(serializer.data)
        
    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        weuser = WEUser.objects.get(user=request.auth.user)
        prompt_typeId = Prompt_Type.objects.get(pk=request.data["prompt_typeId"])
        promptId = Prompt.objects.get(pk=request.data["promptId"])

        prompt_post = PromptPost.objects.create(
            title=request.data["title"],
            content=request.data["content"],
            weuser=weuser,
            prompt_typeId=prompt_typeId,
            promptId=promptId
        )
        serializer = PromptPostSerializer(prompt_post)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        prompt_post = PromptPost.objects.get(pk=pk)
        prompt_post.title = request.data["title"]
        prompt_post.content = request.data["content"]
        

        prompt_typeId = Prompt_Type.objects.get(
            pk=request.data["prompt_typeId"])
        prompt_post.prompt_typeId = prompt_typeId
        
        
        promptId = Prompt.objects.get(
            pk=request.data["promptId"])
        prompt_post.promptId = promptId
        
        prompt_post.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        prompt_post = PromptPost.objects.get(pk=pk)
        prompt_post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


# class CreateLocationPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LocationPost
#         fields = ['id', 'title', 'description',
#                   'locationImg', 'locationId', 'location_type']


class PromptPostSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = PromptPost
        fields = ('id', 'title', 'content',
                  'weuser', 'promptId', 'prompt_typeId')
        depth = 1
