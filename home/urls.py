from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sobre_mim/', views.sobre_mim, name='sobre_mim'),
    path('resumo/', views.resumo, name='resumo'),
    path('servicos/', views.servicos, name='servicos'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contato/', views.contato, name='contato'),
]