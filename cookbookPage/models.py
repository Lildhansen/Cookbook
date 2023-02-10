from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200)
    recipeName = models.ManyToManyField("Recipe")
    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    link = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)
    tagName = models.ManyToManyField(Tag)
    dateAdded = models.DateField()
    def __str__(self):
        return self.name

