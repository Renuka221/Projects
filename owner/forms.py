from django import forms
from .models import CustomUser

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['name', 'username', 'password', 'phone_number', 'address']
        widgets = {
            'password': forms.PasswordInput(),
        }
