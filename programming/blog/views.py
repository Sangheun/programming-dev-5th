from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Post, Comment
from .forms import CommentModelForm

# def post_list(request):
#     return render(request, 'blog/post_list.html', {})

# def about(request):
#     return render(request, 'blog/about.html', {})

def index(request):
    post_list = Post.objects.all()
    context = {
        'post_list':post_list,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {
        'post':post,
    }
    return  render(request, 'blog/post_detail.html', context)

@login_required
def comment_new(request, id):
    if request.method == 'POST':
        form = CommentModelForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, pk=id)
            comment.user = request.user
            comment.save()
            return redirect('blog:post_detail', id)
    else:
        form = CommentModelForm()
    return render(request, 'blog/comment_form.html', {
        'form': form,
        })

@login_required
def comment_edit(request, id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'POST':
        form = CommentModelForm(request.POST, request.FILES, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = get_object_or_404(Post, pk=id)
            comment.user = request.user
            comment.save()
            return redirect('blog:post_detail', id)
    else:
        form = CommentModelForm()
    return render(request, 'blog/comment_form.html', {
        'form': form,
        })

