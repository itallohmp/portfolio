from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def sobre_mim(request):
    return render(request, 'sobre_mim.html')

def contato(request):
    return render(request, 'contato.html')

def servicos(request):
    return render(request, 'servicos.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def resumo(request):
    return render(request, 'resumo.html')