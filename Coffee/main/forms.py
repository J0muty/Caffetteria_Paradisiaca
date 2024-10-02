from django import forms
from .models import RegUser
from datetime import datetime
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
import re


class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}), required=True)
    birthdate = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'DD-MM-YYYY', 'id': 'birthdate'}))

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8 or not re.search(r'[A-Z]', password):
            raise ValidationError('Password must be at least 8 characters long and contain an uppercase letter.')
        return make_password(password)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if RegUser.objects.filter(email=email).exists():
            raise ValidationError('Email is already in use.')
        return email

    def clean_birthdate(self):
        birthdate = self.cleaned_data.get('birthdate')
        if birthdate:
            try:
                return datetime.strptime(birthdate, "%d-%m-%Y").date()
            except ValueError:
                raise ValidationError("Введите правильную дату в формате DD-MM-YYYY.")
        raise ValidationError("Обязательное поле.")

    def save(self):
        user = RegUser(
            firstname=self.cleaned_data['firstname'],
            lastname=self.cleaned_data['lastname'],
            email=self.cleaned_data['email'],
            password=make_password(self.cleaned_data['password']),
            birthdate=self.cleaned_data['birthdate'],
        )
        user.save()
