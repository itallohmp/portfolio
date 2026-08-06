from django.conf import settings
from django.urls import path
from django.views.generic import RedirectView

from home import views

_touch_icon = RedirectView.as_view(
    url=settings.STATIC_URL + 'assets/img/apple-touch-icon.png', permanent=True
)

urlpatterns = [
    path('', views.index, name='index'),
    path('robots.txt', views.robots_txt),
    path('sitemap.xml', views.sitemap_xml),
    path(
        'favicon.ico',
        RedirectView.as_view(url=settings.STATIC_URL + 'assets/img/favicon-new.png', permanent=True),
    ),
    # iOS/Safari pedem estes nomes na raiz do domínio
    path('apple-touch-icon.png', _touch_icon),
    path('apple-touch-icon-precomposed.png', _touch_icon),
    path('apple-touch-icon-120x120.png', _touch_icon),
    path('apple-touch-icon-120x120-precomposed.png', _touch_icon),
]
