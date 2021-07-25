from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('index.urls')),
    path('books', include('books.urls')),
    path('post', include('post.urls')),
    path('contact',include('contact.urls')),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
