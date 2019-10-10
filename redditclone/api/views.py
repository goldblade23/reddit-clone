from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from redditclone.comments.models import Comment
from redditclone.posts.models import Post

from redditclone.api.serializers import CommentSerializer, PostSerializer

class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    basename = 'comment'
    # queryset = Manufacturer.objects.all()
    @action(detail=True, methods=['get'])
    def downvote(self, request, pk):
        comment = Comment.objects.filter(id=pk).first()
        if comment:
            comment.comment_dislikes.add(request.user.reddituser)
            if request.user.reddituser in comment.comment_likes.all():
                comment.comment_likes.remove(request.user.reddituser)
            return Response({
                "status": "Success "
            })
        return Response({
            "status": "Failure"
        })

    @action(detail=True, methods=['get'])
    def upvote(self, request, pk):
        comment = Comment.objects.filter(id=pk).first()
        if comment:
            comment.comment_likes.add(request.user.reddituser)
            if request.user.reddituser in comment.comment_dislikes.all():
                comment.comment_dislikes.remove(request.user.reddituser)
            return Response({
                "status": "Success "
            })
        return Response({
            "status": "Failure"
        })

    @action(detail=True, methods=['get'])
    def unupvote(self, request, pk):
        comment = Comment.objects.filter(id=pk).first()
        if comment:
            comment.comment_likes.remove(request.user.reddituser)
            return Response({
                "status": "Success "
            })
        return Response({
            "status": "Failure"
        })

    @action(detail=True, methods=['get'])
    def undownvote(self, request, pk):
        comment = Comment.objects.filter(id=pk).first()
        if comment:
            comment.comment_dislikes.remove(request.user.reddituser)
            return Response({
                "status": "Success "
            })
        return Response({
            "status": "Failure"
        })

    @action(detail=True, methods=['get'])
    def delete(self, request, pk):
        comment = Comment.objects.filter(id=pk).first()
        if comment:
            comment.comment_removed = True
            comment.save()
            return Response({
                "status": "Success "
            })
        return Response({
            "status": "Failure"
        })


class PostViewSet(ModelViewSet):
    serializer_class = PostSerializer
    basename = 'post'
    # queryset = ShoeType.objects.all()

    @action(detail=True, methods=['get'])
    def downvote(self, request, pk):
        post = Post.objects.filter(id=pk).first()
        if post:
            post.post_dislikes.add(request.user.reddituser)
            if request.user.reddituser in post.post_likes.all():
                post.post_likes.remove(request.user.reddituser)
            return Response({
                "status": "Success "
            })
        return Response({
            "status": "Failure"
        })

    @action(detail=True, methods=['get'])
    def upvote(self, request, pk):
        post = Post.objects.filter(id=pk).first()
        if post:
            post.post_likes.add(request.user.reddituser)
            if request.user.reddituser in post.post_dislikes.all():
                post.post_dislikes.remove(request.user.reddituser)
            return Response({
                "status": "Success "
            })
        return Response({
            "status": "Failure"
        })

    @action(detail=True, methods=['get'])
    def unupvote(self, request, pk):
        post = Post.objects.filter(id=pk).first()
        if post:
            post.post_likes.remove(request.user.reddituser)
            return Response({
                "status": "Success "
            })
        return Response({
            "status": "Failure"
        })

    @action(detail=True, methods=['get'])
    def undownvote(self, request, pk):
        post = Post.objects.filter(id=pk).first()
        if post:
            post.post_dislikes.remove(request.user.reddituser)
            return Response({
                "status": "Success "
            })
        return Response({
            "status": "Failure"
        })

    @action(detail=True, methods=['get'])
    def delete(self, request, pk):
        post = Post.objects.filter(id=pk).first()
        if post:
            post.post_removed = True
            post.save()
            return Response({
                "status": "Success "
            })
        return Response({
            "status": "Failure"
        })


