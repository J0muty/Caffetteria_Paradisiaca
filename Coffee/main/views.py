import json
from datetime import datetime

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseForbidden, JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from .forms import CustomPasswordResetForm
from .forms import RegistrationForm
from .forms import ResetPasswordForm
from .models import RegUser

User = get_user_model()


def index(request):
    return render(request, 'main/index.html')


def coffee(request):
    return render(request, 'main/coffee.html')


def career(request):
    return render(request, 'main/career.html')


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

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error_message = "Вы ввели неверный email или пароль."
            return render(request, 'main/registration/login.html', {'error_message': error_message})

    return render(request, 'main/registration/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('index')


def bonus(request):
    return render(request, 'main/dropdown-menu/bonus.html')


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
    if request.method == 'POST':
        form = CustomPasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                use_https=request.is_secure(),
                email_template_name='main/registration/password_reset_email.txt',
            )
            request.session['password_reset_form_submitted'] = True
            messages.success(request, 'Инструкции по сбросу пароля отправлены на вашу почту.')
            return redirect('password_reset_done')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме.')
    else:
        form = CustomPasswordResetForm()

    return render(request, 'main/registration/password_reset_form.html', {'form': form})


def password_reset_done(request):
    if not request.session.get('password_reset_form_submitted'):
        return HttpResponseForbidden("Access Denied")

    del request.session['password_reset_form_submitted']
    return render(request, 'main/registration/password_reset_done.html')


@login_required
def password_reset_confirm(request):
    user = request.user
    if request.method == 'POST':
        form = ResetPasswordForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пароль успешно сброшен!')
            return redirect('login')
        else:
            messages.error(request, 'Исправьте ошибки в форме.')
    else:
        form = ResetPasswordForm(user=user)

    return render(request, 'main/registration/password_reset_confirm.html', {'form': form})

def send_test_email(request):
    send_mail(
        'Тестовое письмо',
        'Это тестовое письмо от Django.',
        'lololow2017@yandex.ru',
        ['J0muty@mail.ru'],
        fail_silently=False,
    )
    return HttpResponse("Письмо отправлено!")

def password_reset_complete(request):
    referer = request.META.get('HTTP_REFERER')
    if not referer or 'password_reset_confirm' not in referer:
        return HttpResponseForbidden("Access Denied")

    return render(request, 'main/registration/password_reset_complete.html')


def new_password(request):
    return render(request, 'main/registration/new_password.html')


@login_required
def change_settings(request):
    user = request.user
    context = {
        'general_emails': user.general_emails,
        'personalized_emails': user.personalized_emails,
    }
    return render(request, 'main/profile/change.html', context)


@require_POST
@csrf_exempt
@login_required
def update_notification_settings(request):
    user = request.user
    data = json.loads(request.body)
    user.general_emails = data.get('general_emails', False)
    user.personalized_emails = data.get('personalized_emails', False)
    user.save()
    return JsonResponse({'status': 'success'})


@require_POST
@csrf_exempt
@login_required
def toggle_theme(request):
    data = json.loads(request.body)
    user = request.user
    user.dark_mode = data.get('dark_mode', False)
    user.save()
    return JsonResponse({'dark_mode': user.dark_mode})
