from django.shortcuts import render, redirect, loader
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.views.generic import View, UpdateView, ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import View
from django.urls import reverse
from .forms import *
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

def Index(request):
    usuarios = Usuario.objects.all()
    template = loader.get_template('index.html')
    context = {"usuarios" : usuarios}
    
    return HttpResponse(template.render(context,request))

def Projetos(request, *args, **kwargs):
    projetos = Projeto.objects.filter(proprietario_id = kwargs["usuario_id"])
    usuario = kwargs["usuario_id"]
    context = {"projetos": projetos, "usuario" : usuario}
    template = loader.get_template('projetos.html')

    return HttpResponse(template.render(context,request))

def Dashboard(request, *args, **kwargs):
    projeto = Projeto.objects.get(pk = kwargs["projeto_id"])
    context = {"projeto": projeto, "kpsule_form":KpsuleForm, "recurso_form": RecursoForm, "subproduto_form": subProdutoForm}
    template = loader.get_template('dashboard.html')

    return HttpResponse(template.render(context,request))

def ChangeStatus(request, *args, **kwargs):
    capsula = Capsula.objects.get(pk = kwargs["capsula_id"])
    capsula.changeStatus()
    capsula.save()

    return redirect(reverse('dashboard', kwargs={'projeto_id': capsula.subProduto.projeto.pk}))




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
    usuario = 0
    

    def get(self, request,  *args, **kwargs):
        form = ProjetoForm()
        self.usuario = kwargs["usuario_id"]
        return render(request, self.template_name, {'form': form , 'title': self.titulo})

    def post(self,request, *args, **kwargs):
        form = ProjetoForm(request.POST)
        self.usuario = kwargs["usuario_id"]
        if form.is_valid():
            dados_form = form.cleaned_data
            projeto = Projeto(nome=dados_form['nome'], descricao=dados_form['descricao'], escopo=dados_form['escopo'], tempo_estimado=dados_form['tempo_estimado'], orcamento=dados_form['orcamento'], un_tempo=dados_form['un_tempo'], proprietario = Usuario.objects.get(pk = self.usuario))
            projeto.save()
                 
        return redirect(Projetos, usuario_id = kwargs["usuario_id"])


class SubprodutoCreateView(CreateView):
    model = SubProduto
    fields = '__all__'
    form = SubProduto()
    template_name = 'subproduto_form.html'
 
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return redirect(reverse('dashboard', kwargs={'projeto_id': self.object.projeto.pk}))


class RegistrarKpsule(View):
    def post(self, request, *args, **kwargs):
        subProduto = None
        form = KpsuleForm(request.POST)
        if form.is_valid():
            attributes = form.save(commit=False)
            subProduto = attributes.subProduto
            form.save()
        return redirect(reverse('dashboard', kwargs={'projeto_id': subProduto.projeto.pk}))


class RegistrarRecurso(View):
    def post(self, request, *args, **kwargs):
        projeto = None
        form = RecursoForm(request.POST)
        if form.is_valid():
            attributes = form.save(commit=False)
            projeto = attributes.projeto
            form.save()
        return redirect(reverse('dashboard', kwargs={'projeto_id': projeto.pk}))