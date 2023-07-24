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
recipes = Recipe.objects.all()


#maybe add a version of this for recipes if things go badly
def loadTagsFromModel():
    tagsFromModel = Tag.objects.all()#Here we load the tags from the model (different from their representation on the frontend)
    for tag in tagsFromModel:
        if (util.findTagByTagName(tag.name,tags) == None): #the tag is not in the list
            tags.append(TagInAllTagsList(tag.name))
    

    ### need some way to handle such that when refreshing page all pages are set to recipe.isBeingEdited = False (not doing this)
    ### need to add reset to default button instead (maybe also reset all recipes to default - and do recipe.isBeingEdited = False for them all)
            ### måske skal det heddet "undo changes" i stedet 
    ### maybe make such that 1 recipe can only be edited at a time (though this requires that we prompt the user to lose progress in the other one and such)

def main(request):
    loadTagsFromModel()
    recipes = Recipe.objects.all()
    context = {'myTags':tags, 'myRecipes':recipes}
    return render(request, 'index.html',context)

#region tags
def interactWithTag(request):
    tag = util.findTagByTagName(request.POST.get('tagInTagsMenu'),tags)
    tag.selected = not tag.selected
    return(redirect('/'))

def deleteTag(request):
    tagName = request.body.decode('utf-8')
    Tag.objects.filter(name=tagName).delete()
    tagsFromModel = Tag.objects.all()
    print(tagsFromModel)
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
    imageOfRecipeToAdd = request.POST.get("imageOfRecipeToAdd")
    if imageOfRecipeToAdd == "":
        imageOfRecipeToAdd = util.noImageStockPhoto
    tagsToAddToRecipe = request.POST.getlist("tagsToAddToRecipe")
    today = datetime.today().strftime('%Y-%m-%d')
    recipe = Recipe.objects.create(name=nameOfRecipeToAdd,link=linkOfRecipeToAdd,image=imageOfRecipeToAdd,dateAdded=today,isBeingEdited=False)
    print(recipe.image)
    for tag in tagsToAddToRecipe:  
        recipe.tagNames.add(Tag.objects.get(name=tag))   
    return redirect("/")

def showRecipe(request):
    pass

def editRecipe(request):
    recipeId = request.POST.get("recipeId") 
    recipe = Recipe.objects.get(pk=recipeId)
    recipe.isBeingEdited = True
    recipe.save()
    return redirect("/")

def deleteRecipe(request):
    recipeId = request.body.decode('utf-8')
    Recipe.objects.filter(id=recipeId).delete()
    return redirect("/")

def saveEditedRecipe(request):
    nameOfRecipeToEdit = request.POST.get("nameOfRecipeToEdit")
    linkOfRecipeToEdit = request.POST.get("linkOfRecipeToEdit")
    imageOfRecipeToEdit = request.POST.get("imageOfRecipeToEdit")
    tagsOfRecipeToEdit = request.POST.getlist("tagsOfRecipeToEdit")
    idOfRecipeToEdit = request.POST.get("idOfRecipeToEdit")
    
    recipe = Recipe.objects.get(pk=idOfRecipeToEdit)
    if recipe.name != nameOfRecipeToEdit:
        recipe.name = nameOfRecipeToEdit
    if recipe.link != linkOfRecipeToEdit:
        recipe.link = linkOfRecipeToEdit
    if recipe.image != imageOfRecipeToEdit:
        recipe.image = imageOfRecipeToEdit
    if recipe.tagNames != tagsOfRecipeToEdit:
        recipe.tagNames.set(tagsOfRecipeToEdit)
    recipe.isBeingEdited = False
    recipe.save()
    
    return redirect("/") #i guess den kunne returne forskellige redirects (som afgør om den skal resette alle til non-edit mode)

def exitEditing(request):
    idOfRecipeToEdit = request.POST.get("idOfRecipeToEdit")
    recipe = Recipe.objects.get(pk=idOfRecipeToEdit)
    recipe.isBeingEdited = False
    recipe.save()
    return redirect("/")

def exitEditingAllRecipes(request):
    recipes = Recipe.objects.all()
    for recipe in recipes:
        recipe.isBeingEdited = False
        recipe.save()
    return redirect("/")