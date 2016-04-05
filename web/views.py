from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
    #return HttpResponse("Ready to turn some webpages into workflowies?")
	template = loader.get_template('web/index.html')

	return HttpResponse(template.render(context, request))