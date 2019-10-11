from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required

from redditclone.redditUsers.models import RedditUser
from redditclone.comments.models import Comment
from redditclone.communitys.models import Community
from redditclone.posts.models import Post

# from redditclone.redditUsers.forms import UpdateUser




# @login_required()
# def bio(request):
#     html = 'bio.html'
#     #logged_in_user = RedditUser.objects.get(user=request.user)

#     return render(request, html)


def profile_page(request, name, *args, **kwargs):
    html = 'profilepage.html'

    reddituser = RedditUser.objects.get(displayname=name)
    
    posts=Post.objects.filter(author=reddituser)
    p_like_count = 0
    for i in posts:
        p_like_count += i.post_likes.all().count() - i.post_dislikes.all().count()

    comments = Comment.objects.filter(commenter=reddituser)
    c_like_count = 0
    for i in comments:
        c_like_count +=  i.comment_likes.all().count() - i.comment_dislikes.all().count()

    communitys = Community.objects.filter(moderators = reddituser)

    return render(request, html, {'reddituser': reddituser, 'posts': posts, 'post_likes':p_like_count, 'comments': comments, 'comment_likes': c_like_count, 'community_mod':communitys})
