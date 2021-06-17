from django.shortcuts import render, redirect
from .models import Post


# Create your views here.
def index(request):
    return render(request,'main/index.html')


def blog(request):
    postlist = Post.objects.all()
    return render(request, 'main/blog.html', {'postlist': postlist})


def posting(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'main/posting.html', {'post':post})


def new_post(request):
    if request.method == 'POST':
        if request.POST['mainphoto']:
            Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        else:
            Post.objects.create(
                postname=request.POST['postname'],
                contents=request.POST['contents'],
                mainphoto=request.POST['mainphoto'],
            )
        return redirect('/blog/')
    return render(request, 'main/new_post.html')