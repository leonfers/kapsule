# Generated by Django 2.1 on 2018-08-19 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_capsula_ativacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recurso',
            name='quantidade',
        ),
    ]