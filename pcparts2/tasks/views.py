from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Task
from django.http import HttpResponseRedirect
from django.urls import reverse
def tasks(request):
  mytasks = Task.objects.all().values()
  template = loader.get_template('tasks.html')
  context = {
    'mytasks': mytasks,
  }
  return HttpResponse(template.render(context, request))
# Create your views here.
def addtask(request):
  template = loader.get_template('addtask.html')
  return HttpResponse(template.render({}, request))
def addrecord(request):
  x = request.POST['task']
  y = request.POST['deadline']
  task = Task(taskname=x, deadline=y)
  task.save()
  return HttpResponseRedirect(reverse('tasks'))
def delete(request, id):
  task = Task.objects.get(id=id)
  task.delete()
  return HttpResponseRedirect(reverse('tasks'))
def update(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('update.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
def updaterecord(request, id):
  first = request.POST['first']
  last = request.POST['last']
  member = Member.objects.get(id=id)
  member.firstname = first
  member.lastname = last
  member.save()
  return HttpResponseRedirect(reverse('tasks'))
