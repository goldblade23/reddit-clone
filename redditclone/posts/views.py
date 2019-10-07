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

    post = Post.objects.get(id=id)
    current_user = RedditUser.objects.get(user=request.user)
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

    # if request.method == "POST":
    #     replyform = ReplyForm(request.POST)
    #     if replyform.is_valid():
    #         data = replyform.cleaned_data
    #         Comment.objects.create(
    #             post=post,
    #             commenter=current_user,
    #             text=data['text'],
    #             # parent= Comments.objects.get(id=parent_id)
    #             parent= Comment.objects.get(id=1)
    #         )
    #         comment = Comment.objects.get(id=Comment.objects.all().count())
    #         return HttpResponseRedirect('/r/{}/post/{}#c-{}'.format(commun, id, comment.id))
    # replyform = ReplyForm()


    return render(request, html, {'post': post, 'form': form, 'comments': comments})

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

    community = Community.objects.get(name=commun)
    posts = Post.objects.filter(community=community)
    

    comment_count = {}
    for i in posts:
        comments_total = Comment.objects.filter(post=Post.objects.get(id=i.id)).count()
        comment_count[i.id] = comments_total

    
    

    return render(request, html, {'data': posts, "community": community, "count":comment_count})