from django.shortcuts import render

def index(request):
    
    print(dir(request.user))
    
    print(f'User: {request.user}')
    
    if str(request.user) == 'AnonymousUser':
        teste = 'Usuario não logado'
    else:
        teste = 'Usuario logado'
    
    context = {
        'curso': 'programação Web',
        'outro': 'Django é massa',
        'teste': teste
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')