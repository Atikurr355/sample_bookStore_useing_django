from django.urls import path


from .import views

urlpatterns = [
    path('',views.post, name='post'),
    path('blogpost/<str:slug>', views.blogpost, name='blog'),
]
