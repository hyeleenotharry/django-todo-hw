from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo/', views.todo, name='todo'),
    path('todo/delete/<int:id>', views.delete_todo, name='delete-todo'),
    path('todo/<int:id>', views.view_comment,name='view-comment'),
    path('todo/comment/<int:id>', views.write_comment, name='write-comment'),
    path('todo/comment/delete/<int:id>', views.delete_comment, name='delete-comment'),
]