from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
def elements(request):
  template = loader.get_template('elemen.html')
  return HttpResponse(template.render())
def generic(request):
  template = loader.get_template('generic.html')
  return HttpResponse(template.render())