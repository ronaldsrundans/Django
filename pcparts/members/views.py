from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.http import HttpResponseRedirect
from django.urls import reverse
def members(request):
  #template = loader.get_template('index.html')
  #return HttpResponse(template.render())
  mymembers = Member.objects.all().values()
#Member.objects.all().values() 
  template = loader.get_template('members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))
# Create your views here.
def add(request):
  template = loader.get_template('add.html')
  return HttpResponse(template.render({}, request))
def addrecord(request):
  x = request.POST['first']
  y = request.POST['last']
  member = Member(firstname=x, lastname=y)
  member.save()
  return HttpResponseRedirect(reverse('members'))
def delete(request, id):
  member = Member.objects.get(id=id)
  member.delete()
  return HttpResponseRedirect(reverse('members'))
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
  return HttpResponseRedirect(reverse('members'))
