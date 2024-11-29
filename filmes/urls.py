from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_filmes, name='lista_filmes'),
    path('segunda-lista/', views.segunda_lista_filmes, name='segunda_lista_filmes'),  # URL para a segunda lista
    
    path('<int:filme_id>/', views.detalhe_filme, name='detalhe_filme'),
    path('<int:filme_id>/adicionar_review/', views.adicionar_review, name='adicionar_review'),

    path('adicionar/', views.adicionar_filme, name='adicionar_filme'),  # URL para adicionar filmes
    path('<int:filme_id>/deletar/', views.deletar_filme, name='deletar_filme'),  # URL para deletar filme

    path('mover-filme/<int:filme_id>/', views.mover_filme, name='mover_filme'),
]
