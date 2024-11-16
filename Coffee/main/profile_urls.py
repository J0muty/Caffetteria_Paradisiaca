from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.profile, name='profile'),
    path('bonus/', login_required(views.bonus), name='bonus'),
    path('order-history/', login_required(views.order_history), name='order_history'),
    path('personal-info/', login_required(views.personal_info), name='personal_info'),
    path('settings/', login_required(views.settings), name='settings'),
    path('settings/change/', login_required(views.change_settings), name='change_settings'),
    path('settings/support/', login_required(views.support), name='support'),
]
