from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Ready to turn some webpages into workflowies?<br/>Go to https://github.com/ripper234/Web2Workflowy to contribute.")