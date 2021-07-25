from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.core.paginator import Paginator

# Create your views here.

def book(request):
    all_book=Book.objects.all()
    paginator = Paginator(all_book,8, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'page_obj':page_obj,
    }
    return render(request,"books.html",context)
