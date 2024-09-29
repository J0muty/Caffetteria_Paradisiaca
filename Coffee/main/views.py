from django.shortcuts import render


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
    return render(request, 'main/registration/register.html')
