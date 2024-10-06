from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.profile, name='profile'),
    path('my-rewards/', login_required(views.my_rewards), name='my_rewards'),
    path('order-history/', login_required(views.order_history), name='order_history'),
    path('personal-info/', login_required(views.personal_info), name='personal_info'),
    path('settings/', login_required(views.settings), name='settings'),
]
