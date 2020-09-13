from django.db import models


class Task(models.Model):
    STATUS = (
        ('doing', 'Fazendo'),
        ('done', 'Feito'),
    )

    # Criando um campo chamado title que recebe char de no máximo 255 de tamanho
    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )
    # Esse código serve para toda vez que um registro for inserido fique registrado a data
    created_at = models.DateTimeField(auto_now_add=True)
    # Esse código serve para toda vez que um registro for alterado fique registrado a data
    updated_at = models.DateTimeField(auto_now=True)

    #Para mostrar o nome do registro e não o nome do objeto no painel administrativo
    def __str__(self):
        return self.title