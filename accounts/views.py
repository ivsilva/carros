from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout # função para autenticação

def register_view(request):
    if request.method =='POST':
        user_form = UserCreationForm(request.POST) # criamos o form com os dados que o user digitar
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
    else: # Caso for metodo get, só renderizamos a tela normal
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form}) 

def login_view(request):
    if request.method == 'POST':
        username = request.POST["username"] # estou alimentando duas variaveis com os dados que o usuario passar
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password) #o autenticate vai pegar o user e senha e vai retornar se é user registrado no sistema ou não. minha variavel user vai ser alimentada por isso
        if user is not None: #se o user não for nulo, ou seja, se retonou um usuario é sinal que o usuario e existe/valido. então posso fazer o login
            login(request, user) # cria a sessão para nosso usuario
            return redirect('cars_list')
        else:
            login_form = AuthenticationForm()
        return render(request, 'login.html', {'login_form': login_form})
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
    logout (request)
    return redirect("cars_list")