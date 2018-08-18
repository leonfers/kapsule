from django.shortcuts import render, redirect, loader
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.views.generic import View
from django.views.generic.base import View
from .forms import *
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required

def Index(request):
    usuarios = Usuario.objects.all()

    template = loader.get_template('index.html')
    context = {"usuarios" : usuarios}
    
    return HttpResponse(template.render(context,request))

def Projetos(request, *args, **kwargs):
    projetos = Projeto.objects.filter(proprietario_id = kwargs["usuario_id"])
    context = {"projetos":projetos}
    template = loader.get_template('projetos.html')

    return HttpResponse(template.render(context,request))



class RegistrarUsuarioView(View):
    template_name = 'form.html'
    titulo = 'Register'

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, self.template_name, {'form': form , 'title': self.titulo})

    def post(self,request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            dados_form = form.cleaned_data
            usuario = User(username=dados_form['username'], email=dados_form['email'])
            usuario.set_password(dados_form['password'])
            usuario.save()
            perfil = Usuario(user = usuario)
            perfil.save()
            return redirect('index')
        return render(request, self.template_name, {'form':form ,'title': self.titulo})

class RegistrarProjeto(View):
    template_name = 'form_projeto.html'
    titulo = 'Novo Projeto'

    def get(self, request):
        form = ProjetoForm()
        return render(request, self.template_name, {'form': form , 'title': self.titulo})

    def post(self,request):
        form = ProjetoForm(request.POST)
        if form.is_valid():
            dados_form = form.cleaned_data
            projeto = Projeto(nome=dados_form['nome'], descricao=dados_form['descricao'], escopo=dados_form['escopo'], tempo_estimado=dados_form['tempo_estimado'], orcamento=dados_form['orcamento'], un_tempo=dados_form['un_tempo'], proprietario = Usuarios.objects.get(pk = request.usuario.id))
            projeto.save()
                 
        return render(request, self.template_name, {'form':form ,'title': self.titulo})


