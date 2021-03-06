from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import time


TIME_CHOICES = (
        ('seg',1 ),
        ('min',60 ),
        ('h', 3600 ),
        ('d',86400 ),
    )

class Usuario(models.Model):
    nome = models.CharField(max_length=400)
    user = models.OneToOneField('auth.User',related_name='usuario' ,on_delete = models.CASCADE)
    capsula_ativa = models.ForeignKey('Capsula', null=True , on_delete = models.SET_NULL)

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
    
    @property
    def tempo_atual(self):
        tempo = 0
        for sub in self.subprodutos.all():
            for cap in sub.capsulas.all():
                tempo += cap.tempo_gasto

        return tempo
    
    @property
    def custo_atual(self):
        custo = 0
        for sub in self.subprodutos.all():
            for cap in sub.capsulas.all():
                for rec in cap.recursos.all():
                    custo+=rec.custo

        return custo


class Recurso(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name="recursos")
    custo =  models.IntegerField()

    def __str__(self):
        return self.nome


class SubProduto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.CharField(max_length=200)
    tempo_estimado =  models.IntegerField()
    orcamento =  models.IntegerField()
    projeto= models.ForeignKey(Projeto, on_delete=models.CASCADE, related_name="subprodutos")

    def __str__(self):
        return self.nome


class Capsula(models.Model):
    nome = models.CharField(max_length=200)
    ativacao = models.DateTimeField(null = True)
    status = models.BooleanField(default = False)
    descricao = models.CharField(max_length=200)
    tempo_estimado =  models.IntegerField()
    tempo_gasto =  models.IntegerField()
    orcamento =  models.IntegerField()
    subProduto = models.ForeignKey(SubProduto, on_delete=models.CASCADE, related_name="capsulas")
    recursos = models.ManyToManyField(Recurso, null=True)

    def __str__(self):
        return self.nome

    def changeStatus(self):
        if(not self.status ):
            self.ativacao = datetime.now()
            self.subProduto.projeto.proprietario.capsula_ativa = self
            self.subProduto.projeto.proprietario.save()
            self.status = True
        else:
            self.subProduto.projeto.proprietario.capsula_ativa = None
            self.subProduto.projeto.proprietario.save()
            self.tempo_gasto += (datetime.now() - self.ativacao.replace(tzinfo = None)).seconds
            self.ativacao = None
            self.status = False



