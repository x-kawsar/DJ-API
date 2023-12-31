from rest_framework import serializers
from .models import Post
from .forms import PostForm


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['owner','title', 'description']