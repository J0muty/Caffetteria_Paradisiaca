from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from .models import RegUser
from django.db import IntegrityError


def index(request):
    return render(request, 'main/index.html')


def coffee(request):
    return render(request, 'main/coffee.html')


def menu(request):
    return render(request, 'main/menu.html')


def team(request):
    return render(request, 'main/team.html')


def contact(request):
    return render(request, 'main/contact.html')


def application(request):
    return render(request, 'main/application.html')


def profile(request):
    return render(request, 'main/profile.html')


def login(request):
    return render(request, 'main/registration/login.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            reg_user = RegUser(
                firstname=form.cleaned_data['first_name'],
                lastname=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                birthdate=form.cleaned_data['birthdate']  # здесь исправлено
            )
            reg_user.set_password(form.cleaned_data['password'])
            try:
                reg_user.save()
                messages.success(request, 'Ваш аккаунт успешно создан!')
                return redirect('login')
            except IntegrityError:
                form.add_error('email', 'Пользователь с этим адресом электронной почты уже существует.')
        else:
            print(form.errors)  # Убедитесь, что выводите ошибки

    else:
        form = RegistrationForm()

    return render(request, 'main/registration/register.html', {'form': form})
