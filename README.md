# Portfólio — Itallo Polito

Aplicação web de portfólio pessoal com Python/Django no backend e Bootstrap no frontend.
Publicada em produção no PythonAnywhere: https://itallohmp.pythonanywhere.com/

## Stack

- Python 3.12 + Django 6
- HTML5, CSS3, Bootstrap 5, JavaScript
- AOS (animações de scroll) e Typed.js (efeito de digitação)

## Funcionalidades

- Hero com CTAs "Ver projetos" e "Baixar CV"
- Seções: Sobre mim, Carreira (formação + experiência), Habilidades por grupos, Projetos e Contato
- Formulário de contato com envio de e-mail, validação e honeypot anti-spam
- Layout responsivo em tema escuro com acento ciano

## Rodando localmente

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env   # e preencha os valores
python manage.py runserver
```

Configurações sensíveis (SECRET_KEY, credenciais de e-mail) vivem em variáveis de
ambiente carregadas do arquivo `.env` — que nunca é commitado. Em produção, crie um
`.env` equivalente na pasta do projeto (com `DJANGO_DEBUG=False`).
