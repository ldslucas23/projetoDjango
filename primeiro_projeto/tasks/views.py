from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import TaskForm

from .models import Task


# Ao chamar o /helloworld ele vai cair nessa view
def helloWorld(request):
    return HttpResponse('Hello World')


def taskList(request):
    # Com essa variavel eu pego todos os objetos do model Task
    tasks = Task.objects.all().order_by('-created_at')
    return render(request, 'tasks/list.html', {'tasks': tasks})


# Nessa view ele recebe o name como parâmetro
def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})


# Nessa view ele pega os dados de uma tarefa que recebeu o id pelo parâmetro e exibe na página task.html
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})


def newTask(request):
    #Se for inserção
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            #Ao salvar redireciona para a página de listagem de tarefas
            return redirect('/')
    else:
        form = TaskForm
        return render(request, 'tasks/addTask.html', {'form': form})
