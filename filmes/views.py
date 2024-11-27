from django.shortcuts import render, get_object_or_404, redirect
from .models import Filme, Review
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .forms import FilmeForm

def lista_filmes(request):
    filmes = Filme.objects.annotate(media_notas=Avg('reviews__nota'))  # Calcula a média das notas
    return render(request, 'filmes/lista_filmes.html', {
        'filmes': filmes,
        'is_admin': request.user.is_staff  # Passa a informação se o usuário é admin
    })

def detalhe_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    reviews = filme.reviews.all()
    media_notas = reviews.aggregate(media=Avg('nota'))['media']  # Calcula a média das notas

    return render(request, 'filmes/detalhe_filme.html', {
        'filme': filme,
        'reviews': reviews,
        'media_notas': media_notas,  # Passa a média para o template
    })

@login_required
def adicionar_review(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    if request.method == 'POST':
        nota = request.POST['nota']
        comentario = request.POST['comentario']
        Review.objects.create(usuario=request.user, filme=filme, nota=nota, comentario=comentario)
        return redirect('detalhe_filme', filme_id=filme.id)
    return render(request, 'filmes/adicionar_review.html', {'filme': filme})

@login_required
def adicionar_filme(request):
    # Verifica se o usuário é um admin
    if not request.user.is_staff:
        return redirect('lista_filmes')  # Redireciona se não for admin

    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_filmes')  # Redireciona para a lista de filmes após salvar
    else:
        form = FilmeForm()

    return render(request, 'filmes/adicionar_filme.html', {'form': form})