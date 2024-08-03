from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import cpu
from django.http import HttpResponseRedirect
from django.urls import reverse
import datetime
def cpus(request):
  mycpus = cpu.objects.all().values()
  template = loader.get_template('cpuindex.html')
  context = {
    'mycpus': mycpus,
  }
  return HttpResponse(template.render(context, request))
# Create your views here.

def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  z = request.POST['cpumemory']
  a = request.POST['cpuyear']
  cpuvar = cpu(cpuname=x, cpustatus=y, cpumemory=z, cpuyear=a)
  cpuvar.save()
  return HttpResponseRedirect(reverse('cpus'))
def delete(request, id):
  cpuvar = cpu.objects.get(id=id)
  cpuvar.delete()
  return HttpResponseRedirect(reverse('cpus'))
def update(request, id):
  mycpu = cpu.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mycpu': mycpu,
  }
  return HttpResponse(template.render(context, request))
def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  memory = request.POST['cpumemory']
  year = request.POST['cpuyear']
  cpuvar = cpu.objects.get(id=id)
  cpuvar.cpuname = first
  cpuvar.cpustatus = last
  cpuvar.cpumemory = memory
  cpuvar.cpuyear = year
  cpuvar.cpudate = datetime.date.today()
  cpuvar.save()
  return HttpResponseRedirect(reverse('cpus'))
  
