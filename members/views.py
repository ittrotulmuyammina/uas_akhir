from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())
def buy(request):
  template = loader.get_template('buy.html')
  return HttpResponse(template.render())
def elements(request):
  template = loader.get_template('elements.html')
  return HttpResponse(template.render())
def generic(request):
  template = loader.get_template('generic.html')
  return HttpResponse(template.render())

def ina(request):
  template = loader.get_template('ina.html')
  return HttpResponse(template.render())