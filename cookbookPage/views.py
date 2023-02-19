from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.shortcuts import redirect

from .models import Tag
from .classes.TagInAllTagsList import TagInAllTagsList
from .util import utility as util

tagsFromModel = Tag.objects.all()
tags = []
for tag in tagsFromModel:
    print(len(tags))
    tags.append(TagInAllTagsList(tag.name))

def loadTagsFromModel():
    tagsFromModel = Tag.objects.all()
    for tag in tagsFromModel:
        if (util.findTagByTagName(tag.name,tags) == None): #the tag is not in the list
            tags.append(TagInAllTagsList(tag.name))

def main(request):
    context = {'tags':tags}
    return render(request, 'index.html',context)

def interactWithTag(request):
    tag = util.findTagByTagName(request.POST.get('tagInTagsMenu'),tags)
    tag.selected = not tag.selected
    return(redirect('/'))

def deleteTag(request):
    #print(request.POST.get('tagInTagsMenu').value)
    #nu burde et tag kunne blive slettet baseret på dens navn - https://stackoverflow.com/questions/3805958/how-to-delete-a-record-in-django-models
    print("delete the tag plz")
    return(redirect('/'))

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
    newTagName = request.POST.get('addTagInput') 
    Tag.objects.create(name=newTagName)
    loadTagsFromModel()
    return redirect("/")