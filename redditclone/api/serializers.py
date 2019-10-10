from rest_framework.serializers import HyperlinkedModelSerializer

from redditclone.comments.models import Comment
from redditclone.posts.models import Post

class CommentSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'id',
            'comment_likes',
            'comment_dislikes'
            
        )

class PostSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'post_likes',
            'post_dislikes'
        )
