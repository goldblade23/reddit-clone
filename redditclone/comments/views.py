from django.shortcuts import render, HttpResponseRedirect, reverse

from redditclone.comments.forms import commentForm

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