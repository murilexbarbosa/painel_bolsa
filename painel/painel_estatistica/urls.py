from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('retorna_dados_painel', views.retorna_dados_painel, name='retorna_dados_painel')
]