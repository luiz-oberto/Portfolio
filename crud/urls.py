# crud/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_registros, name='listar_registros'),
    path('novo/', views.criar_registro, name='criar_registro'),
    path('editar/<int:pk>/', views.editar_registro, name='editar_registro'),
    path('excluir/<int:pk>/', views.excluir_registro, name='excluir_registro'),
]
