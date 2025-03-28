from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Players

def app(request):
    myplayers = Players.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'Players': myplayers,
    }
    return HttpResponse(template.render(context, request))
