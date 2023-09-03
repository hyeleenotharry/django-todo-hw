from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import todoModel


# Create your views here.
def home(request):
    user = request.user.is_authenticated
    if user:
        return redirect('/todo')
    else:
        return redirect('/signin')

@login_required()
def todo(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            all_todo = todoModel.objects.all().order_by('-created_at')
            return render(request, 'todo/todo.html',{'all_todo': all_todo})
        else:
            return redirect('/signin')
    else:
        user = request.user
        author = user
        content = request.POST.get('content', '')
        title = request.POST.get('title','')
        if title == '' or content == '':
            all_todo = todoModel.objects.all().order_by('-created_at')
            return render(request,'todo/todo.html',{'all_todo': all_todo, 'error': '제목과 내용은 필수입니다!'})
        else:
            my_todo = todoModel.objects.create(content=content, title=title, author=author)
            my_todo.save()
            return redirect('/todo')

@login_required
def delete_todo(request, id):
    my_todo = todoModel.objects.get(id=id)
    my_todo.delete()
    return redirect('/todo')


