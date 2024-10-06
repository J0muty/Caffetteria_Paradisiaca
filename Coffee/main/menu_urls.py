from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.menu, name='menu'),
    path('desserts/', login_required(views.desserts), name='desserts'),
    path('drinks/', login_required(views.drinks), name='drinks'),
    path('combo_and_special_offers/', login_required(views.combo_and_special_offers), name='combo_and_special_offers'),
    path('snacks/', login_required(views.snacks), name='snacks'),
]
