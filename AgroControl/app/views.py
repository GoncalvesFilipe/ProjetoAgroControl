from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Movimento
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.
def index(request):
    return render(request, 'home.html')

def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'catalogo.html', {'produtos': produtos})

@login_required
def produtos_funcionario(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos_funcionario.html', {'produtos': produtos})

def lista_movimentos(request):
    movimentos = Movimento.objects.all()
    return render(request, 'lista_movimentos.html', {'movimentos':movimentos})

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cadastro_usuario = request.POST.get('cadastro')  # você chamou esse campo de "cadastro", mas o nome pode confundir
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirma_senha = request.POST.get('confirma_senha')

        # Validação básica
        if senha != confirma_senha:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'cadastro.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está cadastrado.')
            return render(request, 'cadastro.html')

        # Criação do usuário
        user = User.objects.create_user(
            username=cadastro_usuario,  # ou outro identificador único
            email=email,
            password=senha,
            first_name=nome
        )

        messages.success(request, 'Usuário criado com sucesso!')
        return redirect('login')  # redireciona para página de login

    return render(request, 'cadastro.html')

def adm(request):
    return render(request,'adm.html')