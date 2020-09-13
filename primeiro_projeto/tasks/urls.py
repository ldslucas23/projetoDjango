from django.urls import path
from . import views

urlpatterns = [
    #O endereço /helloworld vai cair em uma view
    path('helloworld/', views.helloWorld),

    #Essa url vai ser a página de home ou seja a /
    #O argumento name pode ser utilizado para chamar essa view em outro lugar do projeto
    path('', views.taskList, name='task-list'),

    #Nessa url passamos um parâmetro pela urll
    path('yourname/<str:name>', views.yourName, name='your-name'),

    #Essa url é utilizada para acessar uma view com os dados da tarefa referente ao id passado por parâmetro
    path('task/<int:id>', views.taskView, name='task-view'),

    # Essa url é utilizada para acessar uma view para inserir uma nova tarefa
    path('newtask/', views.newTask, name='new-task'),

    # Essa url é utilizada para acessar uma view para atualizar os dados de uma tarefa
    path('edit/<int:id>', views.editTask, name='edit-task'),
]