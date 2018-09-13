from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template import loader

from .models import Department, Project

# Create your views here.
def index(request):
    department_list = Department.objects.all()
    context = {'departments': department_list}
    return render(request, 'supervisor/index.html', context)

def projects(request, department_id):
    projects = Project.objects.filter(department_id=department_id)
    return render(request, 'supervisor/projects.html', {'projects': projects})

def project(request, project_id):
    return HttpResponse("You're looking at question %s." % question_id)

def tasks(request, stage_id):
    response = "Tasks for %s."
    return HttpResponse(response % question_id)

def issues(request, task_id):
    return HttpResponse("Issues for the task %s." % question_id)

def issue(request, issue_id):
    return HttpResponse("Issue details for %s." % question_id)



#Dummies ----------------------------------------------------------------------------------------
def testindex(request):
    department_list = Department.objects.all()
    context = {'departments': department_list}
    return render(request, 'test/index.html', context)

def testprojects(request, department_id):
    projects = Project.objects.filter(department_id=department_id)
    return render(request, 'test/projects.html', {'projects': projects})

def testproject(request, project_id):
    return render(request, 'test/project.html', {'projects': projects})

def testtasks(request):
    return render(request, 'test/tasks.html', {'projects': projects})

def testissues(request):
    return render(request, 'test/issues.html', {'projects': projects})