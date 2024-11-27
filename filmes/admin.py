from django.contrib import admin
from .models import Filme

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_criacao')  # Exibe título e data no admin
