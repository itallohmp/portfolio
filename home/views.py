from smtplib import SMTPException

from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render

from contact.forms import ContactForm


def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Honeypot preenchido = bot: responde OK sem enviar nada
            if form.cleaned_data.get('website'):
                return HttpResponse("OK")

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"De: {name} <{email}>\n\n{message}"

            try:
                send_mail(
                    subject,
                    full_message,
                    settings.EMAIL_HOST_USER,
                    ['itallogb@gmail.com'],
                    fail_silently=False,
                )
            except (SMTPException, OSError):
                return HttpResponse(
                    "Não foi possível enviar sua mensagem agora. "
                    "Tente novamente mais tarde ou escreva para itallomp@hotmail.com.",
                    status=502,
                )

            # O validate.js do template espera exatamente "OK" no sucesso
            return HttpResponse("OK")

        return HttpResponse("Verifique os campos preenchidos e tente novamente.", status=400)

    return render(request, "index.html", {"form": ContactForm()})


def robots_txt(request):
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "Disallow: /admin/\n"
        "Sitemap: https://itallohmp.pythonanywhere.com/sitemap.xml\n"
    )
    return HttpResponse(content, content_type="text/plain")


def sitemap_xml(request):
    content = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        '  <url>\n'
        '    <loc>https://itallohmp.pythonanywhere.com/</loc>\n'
        '    <changefreq>monthly</changefreq>\n'
        '    <priority>1.0</priority>\n'
        '  </url>\n'
        '</urlset>\n'
    )
    return HttpResponse(content, content_type="application/xml")
