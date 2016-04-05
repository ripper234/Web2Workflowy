from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Ready to turn some webpages into workflowies?")