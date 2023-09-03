from django.shortcuts import render, redirect

# Create your views here.
def todo(request, id):
    return render(request, 'todo/todo.html')