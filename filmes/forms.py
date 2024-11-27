from django import forms
from .models import Filme, FilmeSegundaLista

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['titulo', 'descricao', 'imagem']  # Ajuste conforme necessário

class FilmeSegundaListaForm(forms.ModelForm):
    class Meta:
        model = FilmeSegundaLista
        fields = ['titulo', 'descricao', 'imagem']