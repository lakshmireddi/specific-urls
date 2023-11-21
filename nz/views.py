from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kane(request):
    return HttpResponse('kane scored 50+ yesterday match')
