from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
#Esse pacote é utilizado para paginar registros na tela
from django.core.paginator import Paginator
#Esse pacote é responsavel por criar formulaŕios com os registros na tela
from .forms import TaskForm
#Esse pacote é utilizado para exibir mensagens para o usuário
from django.contrib import messages
#Esse pacote é utilizado para pegar os dados de um model específico para poder manipular depois
from .models import Task


# Ao chamar o /helloworld ele vai cair nessa view
def helloWorld(request):
    return HttpResponse('Hello World')


def taskList(request):

    # Nessa variavel recebo o parâmetro de pesquisa pelo front. Esse search é o name do meu input de busca no html
    search = request.GET.get('search')
    #Se tiver o caminho pesquisado
    if search:
        #A variável vai ser preenchida pelo que vier no search ignorando o case sentive
        tasks = Task.objects.filter(title__icontains=search)
    #Se não tiver eu continuo mostrando a paginação padrão
    else:
        # Com essa variavel eu pego todos os objetos do model Task
        tasks_list = Task.objects.all().order_by('-created_at')
        #Vai ser exibido 3 registros por página
        paginator = Paginator(tasks_list, 3)
        # Essa variável vai pegar a página atual. Por exemplo a página 3
        page = request.GET.get('page')
        # Se o usuario estiver na página 3 ele vai exibir 3 registros referente a página que ele está, no exemplo 3 registros da página 3
        tasks = paginator.get_page(page)
    return render(request, 'tasks/list.html', {'tasks': tasks})


# Nessa view ele recebe o name como parâmetro
def yourName(request, name):
    return render(request, 'tasks/yourname.html', {'name': name})


# Nessa view ele pega os dados de uma tarefa que recebeu o id pelo parâmetro e exibe na página task.html
def taskView(request, id):
    #Preenchemos essa variável com o model e a primare key, se não achar o objeto ele da um 404 para o usuário
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

# Nessa view ele recebe uma request para redirecionar a paǵina addTask.html para adição de um novo registro
def newTask(request):
    # Se vier um post, a gente salva os dados, esse if é chamado quando o formulário é salvo
    if request.method == 'POST':
        form = TaskForm(request.POST)
        # Se os dados do formulário forem validos ele salva no banco e redireciona para a página inicial
        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            messages.info(request, 'Tarefa salva com sucesso.')
            #Ao salvar redireciona para a página de listagem de tarefas
            return redirect('/')
    # Se não ele continua na mesma página
    else:
        form = TaskForm
        return render(request, 'tasks/addTask.html', {'form': form})

# Nessa view ele recebe uma request para redirecionar a paǵina editTask.html para alterar um registro
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    #Essa variavel ajuda a pré-popular o formulário para podermos editar
    form = TaskForm(instance=task)

    #Se vier um post, a gente salva os dados, esse if é chamado quando o formulário é salvo
    if request.method == 'POST':
        #Ele vai pegar o que vem do post, ou seja os dados alterados
        #O instance vai informar qual registro está sendo alterado
        form = TaskForm(request.POST, instance=task)

        #Se os dados do formulário forem validos ele salva no banco e redireciona para a página inicial
        if form.is_valid():
            task.save()
            messages.info(request, 'Tarefa alterada com sucesso')
            return redirect('/')
        #Se não ele continua na mesma página
        else:
            return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

    #Se não for na hora de salvar, ele vai preencher o formulário com os dados da tarefa, chamado quando a gente clica em editar
    else:
        return render(request, 'tasks/edittask.html', {'form': form, 'task': task})

# Nessa view ele recebe uma request para redirecionar a paǵina para deletar um registro
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()

    messages.info(request, 'Tarefa deletada com sucesso.')
    return redirect('/')

