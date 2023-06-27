from django.urls import path

from . import views

urlpatterns = [
    #tag stuff:
    path('', views.main, name='main'),
    path('deleteTag', views.deleteTag, name="deleteTag"),
    path('interactWithTag', views.interactWithTag, name="interactWithTag"),
    path('selectAllTags', views.selectAllTags, name="selectAllTags"),
    path('deselectAllTags', views.deselectAllTags, name="deselectAllTags"),
    path('addTag', views.addTag, name="addTag"),
    
    #recipe stuff:
    path('addRecipe', views.addRecipe, name="addRecipe"),
    path('editRecipe', views.editRecipe, name="editRecipe"),
    path('saveEditedRecipe', views.saveEditedRecipe, name="saveEditedRecipe"),
    path('exitEditing', views.exitEditing, name="exitEditing"),
    path('exitEditingAllRecipes', views.exitEditingAllRecipes, name="exitEditingAllRecipes"),
    
]