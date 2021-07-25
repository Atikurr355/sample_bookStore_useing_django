from django.shortcuts import render
from .models import Blog

# Create your views here.
def post(request):
    blogs = Blog.objects.all()
    context={
        'blogs': blogs
    }
    return render(request, 'blog.html',context)

def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first 
    context={
        'blog': blog,
    }
    return render(request,"blogpost.html",context)