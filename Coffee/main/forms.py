from django import forms
from django.core.exceptions import ValidationError
from .models import RegUser
from datetime import datetime


class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}), required=True)
    birthdate = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'DD-MM-YYYY', 'id': 'birthdate'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if RegUser.objects.filter(email=email).exists():
            raise ValidationError("Этот адрес электронной почты уже используется.")
        return email

    def clean_birthdate(self):
        birthday = self.cleaned_data.get('birthdate')
        if birthday:
            try:
                return datetime.strptime(birthday, "%d-%m-%Y").date()
            except ValueError:
                raise ValidationError("Введите правильную дату в формате DD-MM-YYYY.")
        raise ValidationError("Обязательное поле.")
