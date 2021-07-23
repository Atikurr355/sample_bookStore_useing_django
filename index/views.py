from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    all_book=Book.objects.all()
    paginator = Paginator(all_book,4, orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'page_obj':page_obj,
    }
    return render(request,'index.html',context)