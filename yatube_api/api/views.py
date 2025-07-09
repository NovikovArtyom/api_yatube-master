from django.shortcuts import render

from rest_framework import viewsets

from posts.models import Group, Post

from .serializers import GroupSerializer, PostSerializer


# Create your views here.
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer