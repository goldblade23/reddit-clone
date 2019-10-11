from django.shortcuts import render, HttpResponseRedirect, reverse

from redditclone.posts.forms import PostLinkForm, PostTextForm
from redditclone.comments.forms import CommentForm, ReplyForm

from redditclone.posts.models import Post
from redditclone.communitys.models import Community
from redditclone.redditUsers.models import RedditUser
from redditclone.comments.models import Comment


# def index(request, *args, **kwargs):
#     html = "Mainpage.html"

#     posts = Post.objects.all()

#     return render(request, html, {'data': posts})

def post_view(request, commun, id, *args, **kwargs):
    html = "postpage.html"

    current_community = Community.objects.get(name=commun)
    post = Post.objects.get(id=id)
    try:
        current_user = RedditUser.objects.get(user=request.user)
    except:
        current_user = False
    comments = Comment.objects.filter(post=post)

    if request.method == "POST":
        form = CommentForm(request.POST)
        # form.parent_id = request.POST.get('parent_id', '')
        # form.save()

        if form.is_valid():
            data = form.cleaned_data
            # parent_id = form.cleaned_data['parent_id']
            # parent_id = request.POST.get('parent_id', '')
            try:
                Comment.objects.create(
                    post=post,
                    commenter=current_user,
                    text=data['text'],
                    parent= Comment.objects.get(id=form.data['comment_id'])
                )
            except:
                Comment.objects.create(
                    post=post,
                    commenter=current_user,
                    text=data['text'],
                )
            comment = Comment.objects.get(id=Comment.objects.all().count())
            return HttpResponseRedirect('/r/{}/post/{}#c-{}'.format(commun, id, comment.id))
    form = CommentForm()

    return render(request, html, {'post': post, 'form': form, 'comments': comments, 'reddituser':current_user, 'community':current_community})

def add_textpost(request, commun, *args, **kwargs):
    html = 'addtextpost.html'

    if request.method == "POST":
        form = PostTextForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                community=Community.objects.get(name=commun),
                author=RedditUser.objects.get(user=request.user),
                title=data['title'],
                text=data['text'],
            )
            return HttpResponseRedirect('/r/{}'.format(commun))
    form = PostTextForm()

    return render(request,html,{'form': form})

def add_linkpost(request, commun, *args, **kwargs):
    html = 'addlinkpost.html'

    if request.method == "POST":
        form = PostLinkForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                community=Community.objects.get(name=commun),
                author=RedditUser.objects.get(user=request.user),
                title=data['title'],
                urls=data['urls'],
            )
            return HttpResponseRedirect('/r/{}'.format(commun))
    form = PostLinkForm()

    return render(request,html,{'form': form})

def post_community_view(request,  commun, *args, **kwargs):
    html = "communitypage.html"
    try:
        current_user = RedditUser.objects.get(user=request.user)
    except:
        current_user = False
    community = Community.objects.get(name=commun)
    posts = Post.objects.filter(community=community).filter(post_removed=False).order_by('-date')

    return render(request, html, {'data': posts, "community": community, "currentuser":current_user})


def post_like(request, id, *args, **kwargs):
    reddit_user = RedditUser.objects.get(user=request.user)
    
    try:
        post = Post.objects.get(id=id)
        
    except Post.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        # return HttpResponseRedirect(reverse('homepage'))

    post.post_likes.add(reddit_user)
    if reddit_user in post.post_dislikes.all():
        post.post_dislikes.remove(reddit_user)
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def post_dislike(request, id, *args, **kwargs):
    reddit_user = RedditUser.objects.get(user=request.user)
    
    try:
        post = Post.objects.get(id=id)
        
    except Post.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        # return HttpResponseRedirect(reverse('homepage'))

    post.post_dislikes.add(reddit_user)
    if reddit_user in post.post_likes.all():
        post.post_likes.remove(reddit_user)
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def post_undislike(request, id, *args, **kwargs):
    reddit_user = RedditUser.objects.get(user=request.user)
    
    try:
        post = Post.objects.get(id=id)
        
    except Post.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        # return HttpResponseRedirect(reverse('homepage'))

    post.post_dislikes.remove(reddit_user)
 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def post_unlike(request, id, *args, **kwargs):
    reddit_user = RedditUser.objects.get(user=request.user)
    
    try:
        post = Post.objects.get(id=id)
        
    except Post.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        # return HttpResponseRedirect(reverse('homepage'))

    post.post_likes.remove(reddit_user)
 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def post_delete(request, commun, id, *args, **kwargs):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
    post.post_removed = True
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))