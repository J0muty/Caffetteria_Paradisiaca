from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import RegUser


class RegUserForm(forms.ModelForm):
    class Meta:
        model = RegUser
        fields = ['login', 'password', 'email', 'firstname', 'lastname', 'birthday']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите логин'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль'
    }))