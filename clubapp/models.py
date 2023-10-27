from django.db import models

# Create your models here.
from django.db import models

class Cookbook(models.Model):
    title = models.CharField(max_length=200)
    book_image = models.ImageField(upload_to='cookbooks/', null=True, blank=True)

class Recipe(models.Model):
    cookbook = models.ForeignKey(Cookbook, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    recipe_image = models.ImageField(upload_to='recipes/', null=True, blank=True)

