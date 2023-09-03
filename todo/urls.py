from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo/', views.todo, name='todo'),
    path('todo/delete/<int:id>', views.delete_todo, name='delete-todo'),
]