from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Cookbook, Recipe

def cookbook_view(request):
    cookbook = Cookbook.objects.last()  # Fetching the latest cookbook
    recipes = Recipe.objects.filter(cookbook=cookbook)
    return render(request, 'clubapp/cookbook.html', {'cookbook': cookbook, 'recipes': recipes})

# ... Your previous views ...
def home_view(request):
  return render(request, 'clubapp/home.html')

def about_view(request):
    return render(request, 'clubapp/about.html')

def books_view(request):
    return render(request, 'clubapp/books.html')

def current_view(request):
    return render(request, 'clubapp/current.html')

def pics_view(request):
    return render(request, 'clubapp/pics.html')

