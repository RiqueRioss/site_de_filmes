import random
from django.shortcuts import render
from filmes.models import FilmeSegundaLista
from django.http import JsonResponse

def roleta(request):
    filmes = FilmeSegundaLista.objects.all()
    
    if not filmes.exists():
        resultado = {"titulo": "Sem filmes", "imagem": "", "descricao": ""}
    else:
        filme = random.choice(filmes)
        resultado = {
            "titulo": filme.titulo,
            "imagem": filme.imagem,  # Certifique-se de que o campo é `imagem`
            "descricao": filme.descricao
        }
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse(resultado)  # Retorna JSON se for uma requisição AJAX
    
    # Renderiza a página para requisições normais (se necessário)
    return render(request, 'roleta_app/roleta.html', {'resultado': resultado})
