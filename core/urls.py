from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bem-vindo/', views.coletar_nome_visitante, name='boas_vindas'),
    path('sair/', views.sair_visitante, name='sair_visitante'),
]
