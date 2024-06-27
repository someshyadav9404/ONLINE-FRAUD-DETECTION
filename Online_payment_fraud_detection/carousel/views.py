from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def carousel(request):
    return HttpResponse("you are my carousel")
