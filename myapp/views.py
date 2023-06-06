from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Project,Task
# Create your views here.

def index(request):
    title = "Prueba 1"
    return render(request,'index.html',{
        "title":title
    })

def hello(request,username):
    return HttpResponse("<h1>Hello world %s</h1>"% username)
def about(request):
    return render(request,'about.html')

def projects(request):
    projects = list(Project.objects.values())
    return render(request,'projects.html')


def tasks(request,name):
    task = Task.objects.get(title=name)
    return render(request,'tasks.html')