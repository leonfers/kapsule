from django import forms
from core.models import Capsula, Recurso

class KpsuleForm(forms.ModelForm):
	recursos = forms.ModelMultipleChoiceField(queryset=Recurso.objects.all(), required=False)

	class Meta:
		model = Capsula
		fields = '__all__'        