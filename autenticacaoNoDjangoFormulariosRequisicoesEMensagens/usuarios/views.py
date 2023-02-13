from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from receitas.models import Receita

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
            messages.error(request, 'As senhas não são iguais')
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            return redirect('cadastro')
        user = User.objects.create_user(username=nome, email=email, password=password)
        user.save()
        messages.success(request, 'Cadastro realizado com sucesso')
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
        id = request.user.id
        receitas = Receita.objects.order_by('-date_receita')\
            .filter(pessoas=id)
        dados = {
            'receitas' : receitas
        }
        return render(request,'usuarios/dashboard.html',dados)
    else:
        return redirect('index')

def logout(request):
    auth_logout(request)
    return redirect('index')

def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        user = get_object_or_404(User, pk=request.user.id)
        receita = Receita(pessoas=user, nome_receita=nome_receita, ingredientes=ingredientes,
         modo_preparo=modo_preparo, tempo_preparo=tempo_preparo, rendimento=rendimento,
         categoria=categoria, foto_receita=foto_receita)
        receita.save()
        return redirect('dashboard')
    else:    
        return render(request, 'usuarios/cria_receita.html')

# Create your views here.
