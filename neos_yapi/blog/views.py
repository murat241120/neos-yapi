from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, PostUpdateForm, CommentForm, CommentUpdateForm
from django.contrib.auth.decorators import login_required

@login_required
def blog(request):
    data = Post.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('blog')
    else:
        form = PostForm()
    context = {
        'data': data,
        'form': form,
    }
    return render(request, 'blog.html', context)

@login_required
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
          instance =  c_form.save(commit=False)
          instance.user = request.user
          instance.post = post
          instance.save()
          return redirect('blog-post-detail', pk=post.id)
    else:
        c_form = CommentForm()
    context = {
        'post': post,
        'c_form': c_form,
    }
    return render(request, 'post_detail.html', context)

@login_required
def post_edit(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = PostUpdateForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blog-post-detail', pk=post.id)
    else:
        form = PostUpdateForm(instance= post)    
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'post_edit.html', context)

@login_required
def post_delete(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('blog')
    context = {
        'post': post,
    }
    return render(request, 'post_delete.html', context)

@login_required
def comment_delete(request, pk):
    comment = Comment.objects.filter(post=pk).last()
    if request.method == 'POST':
        comment.delete()
        return redirect('blog')
    context = {
        'comment': comment,
    }
    return render(request, 'comment_delete.html', context)

@login_required
def comment_edit(request, pk):
    comment = Comment.objects.get(id=pk)
    form = CommentUpdateForm(instance=comment)
    if request.method == 'POST':
        form = CommentUpdateForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('blog')
    context = {'form':form,}
    return render(request, 'comment_edit.html', context)



def search_bar(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        data = Post.objects.filter(title__icontains=searched)
        return render(request, 'search_bar.html',{'searched':searched, 'data':data})
    else:    
        return render(request, 'search_bar.html',{})