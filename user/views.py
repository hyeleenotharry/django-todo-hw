from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import UserModel


# Create your views here.

def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/signup.html')
    elif request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        password2 = request.POST.get('password2', '')
        email = request.POST.get('email','')
        try:
            profile = request.FILES['images']
        except:
            print("파일이 없습니다.")
            profile = None
        if (password != password2):
            return render(request,'user/signup.html', {'error' : '입력하신 비밀번호가 서로 다릅니다!'})
        else:
            ex_user = get_user_model().objects.filter(username=username)
            if ex_user:
                return render(request, 'user/signup.html', {'error': '존재하는 아이디 입니다!'})
            else:
                UserModel.objects.create_user(username=username, password=password, email=email, profile=profile)

            return redirect('/signin')

def sign_in_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/todo')
        else:
            return render(request, 'user/signin.html')
    else:
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        if username == '' or password == '':
            return render(request, 'user/signin.html',{'error' : '아이디와 비밀번호는 필수 입력칸입니다!'})
        else:
            me = auth.authenticate(request, username=username,password=password)
            if me is not None:
                # request.session['username'] = username
                # request.session.set_expiry(0)
                auth.login(request, me)
                return redirect('/todo')
            else:
                return redirect('/signin')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')


