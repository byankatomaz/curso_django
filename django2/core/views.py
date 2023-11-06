from django.shortcuts import render, redirect
from core.forms import ContatoForms, ProdutoModelForm
from django.contrib import messages
from .models import *


def index(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', context)

def contato(request):
    if request.method == 'POST':
        form = ContatoForms(request.POST)
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Email enviado com sucesso')
            return redirect('contato')
        else:
            messages.error(request, 'Erro ao enviar o e-mail')
    else:
        form = ContatoForms()  # Crie um formulário vazio no caso de um pedido GET

    context = {
        'form': form
    }
    return render(request, 'contato.html', context)


def produto(request):
    print(request.user)
    if str(request.user) != 'AnonymousUser':
        if request.method == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            
            if form.is_valid():
                form.save()
                messages.success(request, "Produto salvo com sucesso")
                return redirect('produto')
            else:
                messages.error(request, 'Erro ao salvar o produto')
        else:
            form = ProdutoModelForm()  # Crie um formulário vazio no caso de um pedido GET

        context = {
            'form': form
        }      
        return render(request, 'produto.html', context)
    else:
        return redirect('index')
