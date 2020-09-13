from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        #Nessa variável defino quis os campos que vão aparecer nos formulários
        fields = ('title', 'description')
