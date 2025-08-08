from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.coletar_nome_visitante, name='boas_vindas'), # bem-vindo/
    path('sair/', views.sair_visitante, name='sair_visitante'),
]
