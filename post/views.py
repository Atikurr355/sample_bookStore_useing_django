from django.shortcuts import render,HttpResponse
from .models import Blog
from django.core.paginator import Paginator

# Create your views here.
def post(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs,8, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'page_obj':page_obj,
    }
    return render(request, 'blog.html',context)


def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first 
    context={
        'blog': blog,
    }
    return render(request,"postdetails.html",context)
