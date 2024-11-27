from django.urls import path
from . import views

urlpatterns = [
    path('roleta/', views.roleta, name='roleta'),
]