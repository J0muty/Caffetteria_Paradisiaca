from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('coffee/', views.coffee, name='coffee'),
    path('menu/', views.menu, name='menu'),
    path('сareer/', views.сareer, name='сareer'),
    path('contact/', views.contact, name='contact'),
    path('application/', views.application, name='application'),

    path('profile/', include('main.profile_urls')),
    path('menu/', include('main.menu_urls')),

    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('order-coffee/', views.order_coffee, name='order_coffee'),
    path('reset_password/', views.reset_password, name='reset_password'),
]
