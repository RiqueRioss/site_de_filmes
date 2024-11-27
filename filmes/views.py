from django.shortcuts import render, get_object_or_404, redirect
from .models import Filme, Review
from django.contrib.auth.decorators import login_required

def lista_filmes(request):
    filmes = Filme.objects.all()
    return render(request, 'filmes/lista_filmes.html', {'filmes': filmes})

def detalhe_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    reviews = filme.reviews.all()
    return render(request, 'filmes/detalhe_filme.html', {'filme': filme, 'reviews': reviews})

@login_required
def adicionar_review(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    if request.method == 'POST':
        nota = request.POST['nota']
        comentario = request.POST['comentario']
        Review.objects.create(usuario=request.user, filme=filme, nota=nota, comentario=comentario)
        return redirect('detalhe_filme', filme_id=filme.id)
    return render(request, 'filmes/adicionar_review.html', {'filme': filme})
