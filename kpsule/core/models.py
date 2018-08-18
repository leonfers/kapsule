from django.db import models
from django.contrib.auth.models import User
import datetime


TIME_CHOICES = (
        ('seg',1 ),
        ('min',60 ),
        ('h', 3600 ),
        ('d',86400 ),
    )

class Usuario(models.Model):
    nome = models.CharField(max_length=400)
    user = models.OneToOneField('auth.User',related_name='usuario' ,on_delete = models.CASCADE)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome

    @property
    def email(self):
        return self.user.email
    @property
    def password(self):
        return self.user.password
    @property
    def username(self):
        return self.user.username


class Recurso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    custo =  models.IntegerField()
    quantidade = models.IntegerField(max_length=20)

class Projeto(models.Model):  
    nome = models.CharField(max_length = 500)
    descricao = models.CharField(max_length=3000)
    escopo = models.CharField(max_length=20000)
    tempo_estimado =  models.IntegerField()
    orcamento =  models.IntegerField()
    un_tempo = models.CharField(max_length=5, choices=TIME_CHOICES, default='seg')
    proprietario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class SubProduto(models.Model):
    nome = models.CharField(max_length=200)
    status = models.BooleanField(default = False)
    descricao = models.CharField(max_length=200)
    tempo_estimado =  models.IntegerField()
    orcamento =  models.IntegerField()
    projeto= models.ForeignKey(Projeto, on_delete=models.CASCADE)

class Capsula(models.Model):
    nome = models.CharField(max_length=200)
    status = models.BooleanField(default = False)
    descricao = models.CharField(max_length=200)
    tempo_estimado =  models.IntegerField()
    tempo_gasto =  models.IntegerField()
    orcamento =  models.IntegerField()
    subProduto = models.ForeignKey(SubProduto, on_delete=models.CASCADE)
    recursos = models.ManyToManyField(Recurso)




