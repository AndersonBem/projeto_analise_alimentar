from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .models import Registro, AlimentosConsumidos, Pesagens



##Função que renderiza a pagina principal
@login_required
def index(request):
    return render(request, 'principal/index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('login')
        password = request.POST.get('senha')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('lista_registros') 
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'principal/login.html')




@login_required
def lista_registros(request):
    if request.user.is_superuser:
        registros = Registro.objects.all().order_by('-data', '-hora')
    else:
        registros = Registro.objects.filter(usuario=request.user).order_by('-data', '-hora')
    
    return render(request, 'listas/lista_registros.html', {'registros': registros})