from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def virat(request):
    return HttpResponse('<marquee><h1> virat 80 th century in all formates</marquee></h1>')