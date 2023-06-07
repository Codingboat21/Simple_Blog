from django.shortcuts import render
from .models import Post
# Create your views here.

def index(request):
    posts= Post.objects.all

    return render (request,'index(s).html',{'posts' : posts})

def posts(request,ed):
    posts=Post.objects.get(id=ed)
    return render (request,'posts.html',{"posts":posts})
