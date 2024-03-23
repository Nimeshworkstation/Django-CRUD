from django.forms import ModelForm
from .models import User
from django import forms

class StudentRegistration(ModelForm):
	class Meta:
		model = User
		fields = '__all__'
		widgets = {
		'name': forms.TextInput(attrs={'class': 'form-control'}),
		'email': forms.EmailInput(attrs={'class': 'form-control'}),
		'password': forms.PasswordInput(attrs={'class': 'form-control'})
		}
