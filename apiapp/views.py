from django.shortcuts import render
from rest_framework import generics
from apiapp.models import Post
from apiapp.serializers import PostSerializer

# Create your views here.

class Postlist(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetails (generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
