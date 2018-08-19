from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout

User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def is_valid(self):
        valid = True
        if not super(UserLoginForm, self).is_valid():
            forms.ValidationError('Dados invalidos')
        return valid

class ProjetoForm(forms.Form):
    nome = forms.CharField(max_length = 500)
    descricao = forms.CharField(max_length=3000)
    escopo = forms.CharField(max_length=20000)
    tempo_estimado =  forms.IntegerField()
    orcamento =  forms.IntegerField()
    un_tempo = forms.CharField(max_length=5)

    def clean(self):
        cleaned_data = super(ProjetoForm, self).clean()
        nome = cleaned_data.get('nome')
        escopo = cleaned_data.get('escopo')
        tempo_estimado = cleaned_data.get('tempo_estimado')
        orcamento = cleaned_data.get('orcamento')
        un_tempo = cleaned_data.get('un_tempo')
        if not nome and not escopo and not tempo_estimado and not orcamento and not un_tempo :
            raise forms.ValidationError('Todos os campos são obrigatorios!')

class RecursoForm(forms.Form):
    nome = forms.CharField(max_length = 500)
    descricao = forms.CharField(max_length = 500)
    custo = forms.IntegerField()
    quantidade = forms.IntegerField()

    def clean(self):
        cleaned_data = super(RecursoForm, self).clean()
        nome = cleaned_data.get('nome')
        custo = cleaned_data.get('custo')
        descricao = cleaned_data.get('descricao')
        quantidade = cleaned_data.get('quantidade')

        if not nome and not custo and not descricao and not quantidade :
            raise forms.ValidationError('Todos os campos são obrigatorios!')

class SubprodutoForm(forms.Form):
    nome = forms.CharField(max_length = 500)
    descricao = forms.CharField(max_length = 500)
    tempo_estimado =  forms.IntegerField()
    orcamento = forms.IntegerField()

    def clean(self):
        cleaned_data = super(SubprodutoForm, self).clean()
        nome = cleaned_data.get('nome')
        descricao = cleaned_data.get('descricao')
        tempo_estimado = cleaned_data.get('tempo_estimado')
        orcamento = cleaned_data.get('orcamento')
        if not nome and not orcamento and not descricao and not tempo_estimado :
            raise forms.ValidationError('Todos os campos são obrigatorios!')

class CapsulaForm(forms.Form):
    nome = forms.CharField(max_length = 500)
    status = forms.BooleanField()
    descricao = forms.CharField(max_length = 500)
    tempo_estimado =  forms.IntegerField()
    tempo_gasto =  forms.IntegerField()
    orcamento =  forms.IntegerField()
    
    def clean(self):
        cleaned_data = super(CapsulaForm, self).clean()
        status = cleaned_data.get('status')
        descricao = cleaned_data.get('descricao')
        tempo_estimado = cleaned_data.get('tempo_estimado')
        tempo_gasto = cleaned_data.get('tempo_gasto')
        orcamento = cleaned_data.get('orcamento')
        if not status and not descricao and not tempo_estimado and not orcamento and not tempo_gasto :
            raise forms.ValidationError('Todos os campos são obrigatorios!')

class UserRegistrationForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget = forms.PasswordInput, required=True)
    email = forms.EmailField(required=True)

    def clean_email(self):
        email = self.cleaned_data['email']
        user_exists = User.objects.filter(email=email).exists()
        if user_exists:
            raise forms.ValidationError('Email invalido')
        return email

    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username = username).exists():
            raise forms.ValidationError('Usuário invalido')
        return username

    def is_valid(self):
        valid = True
        if not super(UserRegistrationForm, self).is_valid():
            raise forms.ValidationError('Dados inválidos')

        return valid