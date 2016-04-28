from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
     url(r'^$', 'tabela.views.home', name='home'),
     url(r'^tabela/', 'tabela.views.tabela', name='tabela'),
     url(r'^pogon/', 'tabela.views.pogon', name='pogon'),
     url(r'^legia/', 'tabela.views.legia', name='legia'),
     url(r'^lech/', 'tabela.views.lech', name='lech'),
     url(r'^lechia/', 'tabela.views.lechia', name='lechia'),
     url(r'^slask/', 'tabela.views.slask', name='slask'),
     url(r'^jagiellonia/', 'tabela.views.jagiellonia', name='jagiellonia'),



    url(r'^admin/', include(admin.site.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)