from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template import loader

# Create your views here.
def index(request):
    department_list = list()
    context = {'data': department_list}
    return render(request, 'engineer/index.html', context)

def ongoingprojects(request):
    ongoing_projects_list = list()
    context = {'data': ongoing_projects_list}
    return render(request, 'engineer/ongoingprojects.html', context)

def previousprojects(request):
    previous_projects_list = list()
    context = {'data': previous_projects_list}
    return render(request, 'engineer/previousprojects.html', context)

def milestones(request):
    milestones_projects_list = list()
    context = {'data': milestones_projects_list}
    return render(request, 'engineer/milestones.html', context)

def incidents(request):
    incidents_projects_list = list()
    context = {'data': incidents_projects_list}
    return render(request, 'engineer/incidents.html', context)
