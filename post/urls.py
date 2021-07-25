from django.urls import path


from .import views

urlpatterns = [
    path('',views.post, name='post'),
    path('postdetails/<str:slug>', views.postdetails, name='post'),
]
