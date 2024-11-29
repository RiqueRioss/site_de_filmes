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

        def __init__(self, *args, **kwargs):
            super(FilmeSegundaListaForm, self).__init__(*args, **kwargs)
            
            # Adicionando a classe ao label de 'titulo'
            self.fields['titulo'].label_tag(attrs={'class': 'form-label'})
            
            # Adicionando a classe ao label de 'descricao'
            self.fields['descricao'].label_tag(attrs={'class': 'form-label'})
            
            # Adicionando a classe ao label de 'imagem'
            self.fields['imagem'].label_tag(attrs={'class': 'form-label'})