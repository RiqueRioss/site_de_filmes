from django.shortcuts import render, get_object_or_404, redirect
from .models import Filme, Review
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from .forms import FilmeForm
from django.contrib import messages

def lista_filmes(request):
    filmes = Filme.objects.annotate(media_notas=Avg('reviews__nota'))  # Calcula a média das notas
    return render(request, 'filmes/lista_filmes.html', {
        'filmes': filmes,
        'is_admin': request.user.is_staff  # Passa a informação se o usuário é admin
    })

from .models import FilmeSegundaLista
from .forms import FilmeSegundaListaForm
def segunda_lista_filmes(request):
    filmes = FilmeSegundaLista.objects.all()  # Filmes específicos da segunda lista
    form = FilmeSegundaListaForm()

    # Verifica se o método da requisição é POST, ou seja, se o usuário está enviando um formulário
    if request.method == 'POST':
        form = FilmeSegundaListaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Salva o filme na segunda lista
            return redirect('segunda_lista_filmes')  # Redireciona para a página atual após adicionar o filme

    return render(request, 'filmes/segunda_lista_filmes.html', {'filmes': filmes, 'form': form})

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

@login_required
def deletar_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)

    # Verifica se o usuário é admin
    if not request.user.is_staff:
        messages.error(request, "Você não tem permissão para deletar filmes.")
        return redirect('lista_filmes')  # Redireciona para a lista de filmes se não for admin

    # Deleta o filme e suas reviews
    filme.delete()

    messages.success(request, f'O filme "{filme.titulo}" foi deletado com sucesso!')
    return redirect('lista_filmes')  # Redireciona de volta para a lista de filmes

def mover_filme(request, filme_id):
    # Obter o filme da segunda lista
    filme_segunda_lista = get_object_or_404(FilmeSegundaLista, id=filme_id)

    # Criar o filme na primeira lista
    Filme.objects.create(
        titulo=filme_segunda_lista.titulo,
        imagem=filme_segunda_lista.imagem,
        descricao=filme_segunda_lista.descricao
    )

    # Remover o filme da segunda lista
    filme_segunda_lista.delete()

    # Redirecionar para a segunda lista de filmes
    return redirect('segunda_lista_filmes')