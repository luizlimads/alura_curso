from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def cadastro(request):
    if request.method == 'POST':
        print('Usuário criado com sucesso')
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if not nome.strip():
            return redirect('cadastro')
        if not email.strip():
            return redirect('cadastro')
        if password != password2:
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=password)
        user.save()
        print('usuario cadastro com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == '' or senha == '':
            return redirect('login')
        if User.objects.filter(email=email).exists:
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = authenticate(request,username=nome, password=senha)
            if user is not None:
                auth_login(request, user)
                print('login feito')
                return redirect('dashboard')

    return render(request, 'usuarios/login.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'usuarios/dashboard.html')
    else:
        return redirect('index')

def logout(request):
    auth_logout(request)
    return redirect('index')
# Create your views here.
