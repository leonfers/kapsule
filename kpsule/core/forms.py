from django import forms
from core.models import Capsula, Recurso, SubProduto

class KpsuleForm(forms.ModelForm):
	recursos = forms.ModelMultipleChoiceField(queryset=Recurso.objects.all(), required=False)

	class Meta:
		model = Capsula
		fields = '__all__'        


class RecursoForm(forms.ModelForm):	

	class Meta:
		model = Recurso
		fields = '__all__'        


class subProdutoForm(forms.ModelForm):	

	class Meta:
		model = SubProduto
		fields = '__all__'        