from django.db import models
from django.contrib.auth.models import User

class Filme(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.URLField(blank=True, null=True)  # URL para a imagem do filme
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo

class Review(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    filme = models.ForeignKey(Filme, related_name='reviews', on_delete=models.CASCADE)
    nota = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)])
    comentario = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review de {self.usuario.username} para {self.filme.titulo}"

class FilmeSegundaLista(models.Model):
    titulo = models.CharField(max_length=255)
    imagem = models.URLField(blank=True, null=True)  # URL para a imagem do filme
    descricao = models.TextField()

    def __str__(self):
        return self.titulo