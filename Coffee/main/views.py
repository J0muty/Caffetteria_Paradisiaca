from .forms import RegistrationForm
from .models import RegUser
from django.db import IntegrityError
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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


@login_required(login_url='login')
def profile(request):
    return render(request, 'main/profile.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            reg_user = RegUser(
                firstname=form.cleaned_data['first_name'],
                lastname=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                birthdate=form.cleaned_data['birthdate']
            )
            reg_user.set_password(form.cleaned_data['password'])
            try:
                reg_user.save()
                messages.success(request, 'Ваш аккаунт успешно создан!')
                return redirect('login')
            except IntegrityError:
                form.add_error('email', 'Пользователь с этим адресом электронной почты уже существует.')
        else:
            print(form.errors)

    else:
        form = RegistrationForm()

    return render(request, 'main/registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f"Attempting to authenticate user: {email}")

        user = authenticate(request, username=email, password=password)

        if user is not None:
            if user.is_active:
                print("User is active, logging in.")
                login(request, user)
                messages.success(request, 'Вы успешно вошли в систему!')
                return redirect('profile')
            else:
                print("User account is deactivated.")
                messages.error(request, 'Ваш аккаунт деактивирован.')
        else:
            print("Authentication failed.")
            messages.error(request, 'Неверная почта или пароль.')

    return render(request, 'main/registration/login.html')