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

def login(request):
    return render(request, 'main/login.html')

def signup(request):
    return render(request, 'main/signup.html')