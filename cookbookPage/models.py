from typing import Any
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50,primary_key=True)
    recipeNames = models.ManyToManyField("Recipe")
    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)
    tagNames = models.ManyToManyField(Tag)
    dateAdded = models.DateField()
    def __str__(self):
        return self.name

