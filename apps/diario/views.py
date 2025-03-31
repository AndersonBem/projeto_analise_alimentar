from django.shortcuts import render, redirect
from django.http import HttpResponse



##Função que renderiza a pagina principal
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        # Processar dados do formulário se necessário
        return redirect('index')
    return render(request, 'login.html')
