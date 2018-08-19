from django import forms
from core.models import Capsula, Recurso, SubProduto, Projeto

class KpsuleForm(forms.ModelForm):
	recursos = forms.ModelMultipleChoiceField(queryset=Recurso.objects.all(), required=False)

	class Meta:
		model = Capsula
		fields = '__all__'
		exclude = ['ativacao','status']        


class RecursoForm(forms.ModelForm):	

	class Meta:
		model = Recurso
		fields = '__all__'        


class subProdutoForm(forms.ModelForm):	

	class Meta:
		model = SubProduto
		fields = '__all__'        

class ProjetoForm(forms.ModelForm):	

	class Meta:
		model = Projeto
		fields = '__all__' 
		exclude = ['proprietario']  