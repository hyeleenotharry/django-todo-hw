from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.sign_up_view, name='sign-up'),
    path('signin/', views.sign_in_view, name='sign-in'),
]