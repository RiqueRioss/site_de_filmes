"""
URL configuration for site_de_filmes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from usuarios import views  # Importe as views do seu app "usuarios"
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),  # Inclui as rotas do app "usuarios"
    path('', lambda request: redirect('login'), name='home'),  # Redireciona para a página de login
    path('filmes/', include('filmes.urls')),  # Inclua as rotas do app "filmes"
    path('', include('roleta_app.urls')),# Inclui as rotas do "roleta"
]

