from django.shortcuts import render
from django.http import HttpResponse
from .models import Tag #direct from database - you should not to this in the end!


def index(request):
    a = 10
    tags = Tag.objects.all()
    context = {'tags':tags}
    return render(request, 'index.html',context)
