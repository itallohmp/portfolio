from django.shortcuts import render
from contact.forms import ContactForm  # importa o formulário do app contact
from django.core.mail import send_mail 
from django.conf import settings   
from django.http import HttpResponse


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"De: {name} <{email}>\n\n{message}"

            send_mail(
                subject,
                full_message,
                settings.EMAIL_HOST_USER,
                ['itallogb@gmail.com'],
                fail_silently=False,
            )

            # 👇 ISSO É O QUE O JS DO TEMPLATE ESPERA
            return HttpResponse("OK")

        return HttpResponse("Erro ao enviar", status=400)

    return render(request, "index.html", {"form": ContactForm()})



def sobre_mim(request):
    return render(request, 'sobre_mim.html')

def contato(request):
    # Se você quiser ter uma página separada de contato (contato.html)
    form = ContactForm()
    return render(request, 'contato.html', {"form": form})

def servicos(request):
    return render(request, 'servicos.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def resumo(request):
    return render(request, 'resumo.html')