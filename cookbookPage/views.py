from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    a = 10
    context = {'a':a}
    return render(request, 'index.html',context)
