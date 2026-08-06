from django.conf import settings
from django.urls import path
from django.views.generic import RedirectView

from home import views


urlpatterns = [
    path('', views.index, name='index'),
    path(
        'favicon.ico',
        RedirectView.as_view(url=settings.STATIC_URL + 'assets/img/favicon-new.png', permanent=True),
    ),
]
