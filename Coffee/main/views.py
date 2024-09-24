from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, views as auth_views
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import RegUserForm, LoginForm


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

def signup(request):
    if request.method == 'POST':
        form = RegUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                auth_login(request, user)
                return redirect('profile')
    else:
        form = RegUserForm()
    return render(request, 'main/signup.html', {'form': form})

class CustomLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'main/login.html'
    next_page = reverse_lazy('profile')


@login_required
def profile_view(request):
    return render(request, 'main/profile.html')