# Generated by Django 2.2.16 on 2020-09-15 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_remove_task_importante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.CharField(choices=[('doing', 'Fazendo'), ('done', 'Feito')], default='doing', max_length=5),
        ),
    ]
