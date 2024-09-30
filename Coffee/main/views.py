from .forms import RegistrationForm
from .models import RegUser
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
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
    print(f"User authenticated: {request.user.is_authenticated}")
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
                return redirect('profile')
            else:
                print("User account is deactivated.")
        else:
            print("Authentication failed.")

    return render(request, 'main/registration/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')


def manage_cards(request):
    return render(request, 'main/dropdown-menu/manage_cards.html')


def my_rewards(request):
    return render(request, 'main/dropdown-menu/my_rewards.html')


def order_coffee(request):
    return render(request, 'main/dropdown-menu/order_coffee.html')


def order_history(request):
    return render(request, 'main/dropdown-menu/order_history.html')


@login_required
def personal_info(request):
    user = request.user
    context = {
        'firstname': user.firstname,
        'lastname': user.lastname,
        'birthdate': user.birthdate,
    }
    return render(request, 'main/dropdown-menu/personal_info.html', context)


@login_required
def settings(request):
    user = request.user
    context = {
        'email': user.email,
    }
    return render(request, 'main/dropdown-menu/settings.html', context)
