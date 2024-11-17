from django import forms
from .models import RegUser
from datetime import datetime
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.forms import PasswordResetForm


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
            raise ValidationError('Пароль должен иметь длину не менее 8 символов и содержать заглавную букву.')
        return password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if RegUser.objects.filter(email=email).exists():
            raise ValidationError('Эта почта уже используется')
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
            firstname=self.cleaned_data['first_name'],
            lastname=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            birthdate=self.cleaned_data['birthdate'],
        )
        user.save()


class ResetPasswordForm(SetPasswordForm):
    class Meta:
        model = RegUser
        fields = ['new_password1', 'new_password2']

    def clean_new_password1(self):
        password = self.cleaned_data.get('new_password1')
        if self.instance.check_password(password):
            raise forms.ValidationError("Новый пароль не может совпадать с текущим.")
        return password


class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not RegUser.objects.filter(email=email).exists():
            raise ValidationError("Пользователь с таким email не зарегистрирован.")
        return email


class SupportForm(forms.Form):
    name = forms.CharField(max_length=100, label='Ваше имя', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите ваше имя',
    }))
    email = forms.EmailField(label='Ваш электронный адрес', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите ваш email',
    }))
    subject = forms.CharField(max_length=150, label='Тема обращения', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите тему обращения',
    }))
    message = forms.CharField(label='Ваше сообщение', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Введите ваше сообщение',
        'rows': 5,
    }))

