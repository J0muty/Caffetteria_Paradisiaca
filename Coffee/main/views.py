from .forms import RegistrationForm
from .models import RegUser
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.http import HttpResponse

User = get_user_model()


def index(request):
    return render(request, 'main/index.html')


def coffee(request):
    return render(request, 'main/coffee.html')


def сareer(request):
    return render(request, 'main/сareer.html')


def contact(request):
    current_year = datetime.now().year
    return render(request, 'main/contact.html', {'current_year': current_year})


def application(request):
    return render(request, 'main/application.html')


@login_required(login_url='login')
def profile(request):
    user = request.user
    context = {
        'firstname': user.firstname,
        'lastname': user.lastname,
    }
    print(f"User authenticated: {request.user.is_authenticated}")
    return render(request, 'main/profile.html', context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            reg_user = RegUser(
                firstname=form.cleaned_data['first_name'],
                lastname=form.cleaned_data['last_name'],
                email=form.cleaned_data['email'],
                birthdate=form.cleaned_data['birthdate'],
            )
            reg_user.set_password(form.cleaned_data['password'])
            reg_user.save()
            return redirect('login')
    else:
        form = RegistrationForm()

    return render(request, 'main/registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                login(request, user)
                return redirect('index')
        except User.DoesNotExist:
            pass

        error_message = "Вы ввели неверный email или пароль."
        print(error_message)
        return render(request, 'main/registration/login.html', {'error_message': error_message})

    return render(request, 'main/registration/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')


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


def menu(request):
    return render(request, 'main/menu.html')


@login_required
def desserts(request):
    return render(request, 'main/menu/desserts.html')


@login_required
def drinks(request):
    return render(request, 'main/menu/drinks.html')


@login_required
def combo_and_special_offers(request):
    return render(request, 'main/menu/combo_and_special_offers.html')


@login_required
def snacks(request):
    return render(request, 'main/menu/snacks.html')


def password_reset_form(request):
    return render(request, 'main/registration/password_reset_form.html')


def send_test_email(request):
    send_mail(
        'Тестовое письмо',
        'Это тестовое письмо от Django.',
        'lololow2017@yandex.ru',
        ['J0muty@mail.ru'],
        fail_silently=False,
    )
    return HttpResponse("Письмо отправлено!")


def new_password(request):
    return render(request, 'main/registration/new_password.html')


@login_required
def change_settings(request):
    return render(request, 'main/profile/change.html')
