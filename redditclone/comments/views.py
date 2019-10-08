from django.shortcuts import render, HttpResponseRedirect, reverse

from redditclone.comments.forms import CommentForm

from redditclone.comments.models import Comment
from redditclone.redditUsers.models import RedditUser

def comments_post(request, commun, *args, **kwargs):
    html = 'addtextpost.html'

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Comment.objects.create(
                text=data['text'],
            )
            return HttpResponseRedirect('/r/{}'.format(commun))
    form = CommentForm()

    return render(request,html,{'form': form})

def comments_like(request, commun, id, *args, **kwargs):
    reddit_user = RedditUser.objects.get(user=request.user)
    
    try:
        comment = Comment.objects.get(id=id)
        
    except Comment.DoesNotExist:
        return HttpResponseRedirect('/r/{}/post/{}#c-{}'.format(commun, comment.post.id, comment.id))
        # return HttpResponseRedirect(reverse('homepage'))

    comment.comment_likes.add(reddit_user)
    if reddit_user in comment.comment_dislikes.all():
        comment.comment_dislikes.remove(reddit_user)
        
    return HttpResponseRedirect('/r/{}/post/{}#c-{}'.format(commun, comment.post.id, comment.id))

def comments_dislike(request, commun, id, *args, **kwargs):
    reddit_user = RedditUser.objects.get(user=request.user)
    
    try:
        comment = Comment.objects.get(id=id)
        
    except Comment.DoesNotExist:
        return HttpResponseRedirect('/r/{}/post/{}#c-{}'.format(commun, comment.post.id, comment.id))
        # return HttpResponseRedirect(reverse('homepage'))

    comment.comment_dislikes.add(reddit_user)
    if reddit_user in comment.comment_likes.all():
        comment.comment_likes.remove(reddit_user)
        
    return HttpResponseRedirect('/r/{}/post/{}#c-{}'.format(commun, comment.post.id, comment.id))

def comments_undislike(request, commun, id, *args, **kwargs):
    reddit_user = RedditUser.objects.get(user=request.user)
    
    try:
        comment = Comment.objects.get(id=id)
        
    except Comment.DoesNotExist:
        return HttpResponseRedirect('/r/{}/post/{}#c-{}'.format(commun, comment.post.id, comment.id))
        # return HttpResponseRedirect(reverse('homepage'))

    comment.comment_dislikes.remove(reddit_user)
 
    return HttpResponseRedirect('/r/{}/post/{}#c-{}'.format(commun, comment.post.id, comment.id))

def comments_unlike(request, commun, id, *args, **kwargs):
    reddit_user = RedditUser.objects.get(user=request.user)
    
    try:
        comment = Comment.objects.get(id=id)
        
    except Comment.DoesNotExist:
        return HttpResponseRedirect('/r/{}/post/{}#c-{}'.format(commun, comment.post.id, comment.id))
        # return HttpResponseRedirect(reverse('homepage'))

    comment.comment_likes.remove(reddit_user)
 
    return HttpResponseRedirect('/r/{}/post/{}#c-{}'.format(commun, comment.post.id, comment.id))

# def comments_comments(request, commun, *args, **kwargs):
#     html = 'addtextpost.html'

#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             Comment.objects.create(
#                 text=data['text'],
#             )
#             return HttpResponseRedirect('/r/{}'.format(commun))
#     form = CommentForm()

#     return render(request,html,{'form': form})