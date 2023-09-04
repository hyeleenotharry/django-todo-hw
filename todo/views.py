from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .models import todoModel, todoComment


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

@login_required
def view_comment(request, id):
    my_todo = todoModel.objects.get(id=id)
    all_comment = todoComment.objects.all().filter(todo_id=id)
    return render(request,'todo/todo_detail.html',{'my_todo' : my_todo, 'all_comment' : all_comment})

@login_required
def write_comment(request, id):
    re_add = reverse('view-comment', args=(id,))

    user = request.user
    my_comment = todoComment()
    my_comment.comment = request.POST.get('comment','')
    my_comment.author = user
    my_comment.todo_id = id
    if my_comment.comment == '':
        print('not blank')
        return redirect(re_add)
    else:
        print('comment well written')
        my_comment.save()
        return redirect(re_add)

@login_required
def delete_comment(request, id):
    my_comment = todoComment.objects.get(id=id)
    re_add = reverse('view-comment',args=(my_comment.todo_id,))
    my_comment.delete()
    return redirect(re_add)

@login_required
def my_todolist(request):
    user = request.user
    my_todolist = todoModel.objects.all().filter(author=user)
    return render(request, 'todo/my_todolist.html', {'my_todolist': my_todolist})

@login_required
def update_todo(request, id):
    exist_todo = todoModel.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'todo/update_todo.html', {'exist_todo': exist_todo})
    if request.method == 'POST':
        title = request.POST['new_title']
        content = request.POST['new_content']
        if title == '' or content == '':
            return render(request,'todo/update_todo.html', {'error' : '제목과 내용은 필수 요소입니다.'})
        else:
            exist_todo.title = title
            exist_todo.content = content
            exist_todo.save()
            return redirect('/todo/mytodo')

@login_required
def check_todo(request, id):
    checklist = request.POST.getlist('todo-check')

    if checklist:
        print(checklist)
        for i in checklist:
            todo = todoModel.objects.get(id=i)
            todo.is_completed = True
            todo.save()
    else:
        checklist = request.POST.getlist('todo-check2')
        print(checklist)
        for i in checklist:
            todo = todoModel.objects.get(id=i)
            todo.is_completed = False
            todo.save()
    return redirect('/todo/mytodo')
