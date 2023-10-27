from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('books/', views.books_view, name='books'),
    path('current/', views.current_view, name='current'),
    path('pics/', views.pics_view, name='pics'),
]
