from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Task

#Ao chamar o /helloworld ele vai cair nessa view
def helloWorld(request):
    return HttpResponse('Hello World')

def taskList(request):
    #Com essa variavel eu pego todos os objetos do model Task
    tasks = Task.objects.all()
    return render(request, 'tasks/list.html', {'tasks': tasks})

#Nessa view ele recebe o name como parâmetro
def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name' : name})

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})