"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.core.exceptions import ValidationError
from writersedgeapi.models import Post
from writersedgeapi.models.WEUser import WEUser


class PostView(ViewSet):

    def retrieve(self, request, pk):
        posts = Post.objects.get(pk=pk)
        serializer = PostSerializer(posts)
        return Response(serializer.data)

    def list(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns
            Response -- JSON serialized game instance
        """
        weuser = WEUser.objects.get(user=request.auth.user)

        post = Post.objects.create(
            title=request.data["title"],
            content=request.data["content"],
            weuser=weuser
        )
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests for a game

        Returns:
            Response -- Empty body with 204 status code
        """

        post = Post.objects.get(pk=pk)
        post.title = request.data["title"]
        post.content = request.data["content"]

        post.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


# class CreateLocationPostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = LocationPost
#         fields = ['id', 'title', 'description',
#                   'locationImg', 'locationId', 'location_type']


class PostSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Post
        fields = ('id', 'title', 'content',
                  'weuser')
        depth = 1
