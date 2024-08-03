from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import hdd
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
def hdds(request):
  #template = loader.get_template('index.html')
  #return HttpResponse(template.render())
  myhdds = hdd.objects.all().values()
#hdd.objects.all().values() 
  template = loader.get_template('index.html')
  context = {
    'myhdds': myhdds,
  }
  return HttpResponse(template.render(context, request))
# Create your views here.

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  z = request.POST['hddmemory']
  a = request.POST['hddyear']
  hddvar = hdd(hddname=x, hddstatus=y, hddmemory=z, hddyear=a)
  hddvar.save()
  return HttpResponseRedirect(reverse('hdds'))
def delete(request, id):
  hddvar = hdd.objects.get(id=id)
  hddvar.delete()
  return HttpResponseRedirect(reverse('hdds'))
def update(request, id):
  myhdd = hdd.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'myhdd': myhdd,
  }
  return HttpResponse(template.render(context, request))
def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  memory = request.POST['hddmemory']
  year = request.POST['hddyear']
  hddvar = hdd.objects.get(id=id)
  hddvar.hddname = first
  hddvar.hddstatus = last
  hddvar.hddmemory = memory
  hddvar.hddyear = year
  hddvar.hdddate = datetime.date.today()
  hddvar.save()
  return HttpResponseRedirect(reverse('hdds'))
  
