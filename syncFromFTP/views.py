from django.http import HttpResponse
from django.shortcuts import render



def WelcomeMessage(request):
    return HttpResponse("<h1> Hello USADA </h1>")