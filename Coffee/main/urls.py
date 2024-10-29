from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('coffee/', views.coffee, name='coffee'),
    path('menu/', views.menu, name='menu'),
    path('career/', views.career, name='career'),
    path('contact/', views.contact, name='contact'),
    path('application/', views.application, name='application'),

    path('profile/', include('main.profile_urls')),
    path('menu/', include('main.menu_urls')),

    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('order-coffee/', views.order_coffee, name='order_coffee'),

    path('password_reset_form/', views.password_reset_form, name='password_reset_form'),
    path('password_reset/done/', views.password_reset_done, name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='main/registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/', views.password_reset_complete, name='password_reset_complete'),


    path('toggle-theme/', views.toggle_theme, name='toggle_theme'),
    path('update_notification_settings/', views.update_notification_settings, name='update_notification_settings'),
]
