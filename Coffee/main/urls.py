from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coffee/', views.coffee, name='coffee'),
    path('menu/', views.menu, name='menu'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('application/', views.application, name='application'),
    path('login/', views.login, name='login'),
    path('register/', views.signup, name='signup')
]
