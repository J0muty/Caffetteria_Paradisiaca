from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coffee/', views.coffee, name='coffee'),
    path('menu/', views.menu, name='menu'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('application/', views.application, name='application'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
