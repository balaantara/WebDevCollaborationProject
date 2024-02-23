from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def test(request):
    templates = loader.get_template('data/templates/index.html')
    return HttpResponse(templates.render())
