from django import forms
from .models import Administrador

class formLog(forms.ModelForm):
	class Meta:
		model = Administrador
		fields = ['usuario','contrasenia']