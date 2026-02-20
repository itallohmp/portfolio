from django.urls import path
from home import views
from contact.views import contact_view


urlpatterns = [
    path('', views.index, name='index'),
    path('sobre_mim/', views.sobre_mim, name='sobre_mim'),
    path('resumo/', views.resumo, name='resumo'),
    path('servicos/', views.servicos, name='servicos'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contato/', views.contato, name='contato'),
    path("contact/", contact_view, name="contact"),

]