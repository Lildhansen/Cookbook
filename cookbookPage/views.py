from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.shortcuts import redirect


from datetime import datetime
import time


from .models import Tag
from .models import Recipe
from .classes.TagInAllTagsList import TagInAllTagsList
from .util import utility as util

tagsFromModel = Tag.objects.all()
tags = []

def loadTagsFromModel():
    tagsFromModel = Tag.objects.all()#Here we load the tags from the model (different from their representation on the frontend)
    for tag in tagsFromModel:
        if (util.findTagByTagName(tag.name,tags) == None): #the tag is not in the list
            tags.append(TagInAllTagsList(tag.name))
    
def main(request):
    loadTagsFromModel()
    context = {'myTags':tags}
    return render(request, 'index.html',context)

#tag stuff
#region tags
def interactWithTag(request):
    tag = util.findTagByTagName(request.POST.get('tagInTagsMenu'),tags)
    tag.selected = not tag.selected
    return(redirect('/'))

def deleteTag(request):
    tagName = request.body.decode('utf-8')
    Tag.objects.filter(name=tagName).delete()
    tagsFromModel = Tag.objects.all()
    for tag in tags: 
        if util.findTagByTagName(tag.name,tagsFromModel) == None: #if the tag from the original list is not in the model, it has been deleted
            tags.remove(tag)
    return(redirect("/"))

def selectAllTags(request):
    loadTagsFromModel()
    for tag in tags:
        tag.selected = True 
    return(redirect('/'))

def deselectAllTags(request):
    loadTagsFromModel()
    for tag in tags:
        tag.selected = False
    return(redirect('/'))

def addTag(request):
    newTagName = request.POST.get('addTagInput').capitalize().strip()
    Tag.objects.create(name=newTagName)
    return redirect("/")

#endregion

def addRecipe(request):
    nameOfRecipeToAdd = request.POST.get("nameOfRecipeToAdd")
    linkOfRecipeToAdd = request.POST.get("linkOfRecipeToAdd")
    today = datetime.today().strftime('%Y-%m-%d')
    print(nameOfRecipeToAdd,linkOfRecipeToAdd)
    Recipe.objects.create(name=nameOfRecipeToAdd,link=linkOfRecipeToAdd,dateAdded=today)
    return redirect("/")