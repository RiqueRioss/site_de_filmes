import random
from django.shortcuts import render
from filmes.models import Filme

def roleta(request):
    # Configuração da roleta (filmes)
    filmes = Filme.objects.all()
    
    if not filmes.exists():
        resultado = "Sem filmes"
    else:
        resultado = random.choice(filmes)
    
    # Renderiza a página e passa o resultado como contexto
    return render(request, 'roleta_app/roleta.html', {'resultado': resultado})
