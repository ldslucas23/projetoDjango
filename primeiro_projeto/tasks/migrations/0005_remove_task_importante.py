# Generated by Django 2.2.16 on 2020-09-15 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_importante'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='importante',
        ),
    ]
