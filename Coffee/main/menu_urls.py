from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.menu, name='menu'),
    path('desserts/', login_required(views.desserts), name='desserts'),
    path('drinks/', login_required(views.drinks), name='drinks'),
    path('special_offers/', login_required(views.special_offers), name='special_offers'),
    path('snacks/', login_required(views.snacks), name='snacks'),
]
