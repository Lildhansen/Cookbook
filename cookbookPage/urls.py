from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('deleteTag', views.deleteTag, name="deleteTag"),
    path('interactWithTag', views.interactWithTag, name="interactWithTag"),
    path('selectAllTags', views.selectAllTags, name="selectAllTags"),
    path('deselectAllTags', views.deselectAllTags, name="deselectAllTags"),
    path('addTag', views.addTag, name="addTag"),
]