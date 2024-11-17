from django import forms
from .models import CustomUser

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('email','username','password')
    
# Adicionar validações caso necessário.