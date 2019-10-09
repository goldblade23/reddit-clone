# from rest_framework.viewsets import ModelViewSet
# from rest_framework.decorators import action

# from redditclone.comments.models import Comment
# from redditclone.posts.models import Post

# from redditclone.api.serializers import CommentSerializer, PostSerializer

# class CommentViewSet(ModelViewSet):
#     serializer_class = CommentSerializer
#     basename = 'comment'
#     # queryset = Manufacturer.objects.all()

# class PostViewSet(ModelViewSet):
#     serializer_class = PostSerializer
#     basename = 'post'
#     # queryset = ShoeType.objects.all()

#     @action(detail=True, methods=['get'])
#     def upvote(self, request, pk):
#         post = Post.objects.get(id=pk)
#         if post:
#             post.likes +=1
#             post.save()
#             return Response({
#                 "status": "Success "
#             })
#         return Response({
#                 "status": "Failure"
#             })

    # @action(detail=True, methods=['get'])
    # def upvote(self, request, pk):
    #     post = Post.objects.filter(id=pk).first()
    #     if post:
    #         post.post_likes.add(request.user.reddituser)
    #         if request.user.reddituser in post.post_dislikes.all():
    #             post.post_dislikes.remove(request.user.reddituser)
    #         return Response({
    #             "status": "Success "
    #         })
    #     return Response({
    #         "status": "Failure"
    #     })

