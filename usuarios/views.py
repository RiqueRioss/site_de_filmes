from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# VIEW DO CADASTRO
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password != password_confirm:
            messages.error(request, "As senhas não coincidem.")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Nome de usuário já existe.")
            return redirect('register')

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Cadastro realizado com sucesso! Faça login.")
        return redirect('login')

    return render(request, 'usuarios/register.html')

# VIEW DO LOGIN
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('lista_filmes')  # Redireciona para a lista de filmes
        else:
            messages.error(request, 'Usuário ou senha inválidos.')  # Exibe mensagem de erro

    return render(request, 'usuarios/login.html')

# VIEW DO LOGOUT
def user_logout(request):
    logout(request)
    messages.success(request, "Logout realizado com sucesso!")
    return redirect('login')