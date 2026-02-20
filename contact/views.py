from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Aqui você pode enviar email ou salvar no banco
            return render(request, "contact_success.html")
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form": form})