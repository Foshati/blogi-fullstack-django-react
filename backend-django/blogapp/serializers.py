from rest_framework import serializers
from .models import Post 


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ["id", "title", "content", "slug"]


# get_recent_blogs = http://127.0.0.1:8008/blogs/recent
# sepecific_blog = http://127.0.0.1:8008/blogs/:slug