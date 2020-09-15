from django.db import models
#Pegar o model do usuário
from django.contrib.auth import get_user_model

class Task(models.Model):
    STATUS = (
        ('doing', 'Fazendo'),
        ('done', 'Feito')
    )

    # Criando um campo chamado title que recebe char de no máximo 255 de tamanho
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    done = models.CharField(
        max_length=5,
        choices=STATUS,
        default='doing'
    )
    #Atelamos o model do usuário a tarefa, ao deletar o usuário todas as tarefas vão ser deletadas
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    # Esse código serve para toda vez que um registro for inserido fique registrado a data
    created_at = models.DateTimeField(auto_now_add=True)
    # Esse código serve para toda vez que um registro for alterado fique registrado a data
    updated_at = models.DateTimeField(auto_now=True)

    #Para mostrar o nome do registro e não o nome do objeto no painel administrativo
    def __str__(self):
        return self.title