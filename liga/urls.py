from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    # Examples:
   #  url(r'^$', 'tabela.views.home', name='home'),
     url(r'^$', 'tabela.views.post_list', name='list'),
     url(r'^tabela/', 'tabela.views.tabela', name='tabela'),
     url(r'^druzyny/', 'tabela.views.druzyny', name='druzyny'),
     url(r'^widownia/', 'tabela.views.home', name='home'),
     url(r'^strzelcy/', 'tabela.views.tabela_strzelcow', name='tabela_strzelcow'),


     # blog/post
    # url(r'^post/', 'tabela.views.post_list', name='list'),
     url(r'^create/', 'tabela.views.post_create', name='post_create'),
     url(r'^detail/(?P<id>\d+)/$', 'tabela.views.post_detail', name='detail'),
     url(r'^detail/(?P<id>\d+)/edit/$', 'tabela.views.post_update', name='edit'),
     url(r'^detail/(?P<id>\d+)/delete/$', 'tabela.views.post_delete', name='post_delete'),


     # kluby
     url(r'^pogon/', 'tabela.views.pogon', name='pogon'),
     url(r'^legia/', 'tabela.views.legia', name='legia'),
     url(r'^lech/', 'tabela.views.lech', name='lech'),
     url(r'^lechia/', 'tabela.views.lechia', name='lechia'),
     url(r'^slask/', 'tabela.views.slask', name='slask'),
     url(r'^jagiellonia/', 'tabela.views.jagiellonia', name='jagiellonia'),
     url(r'^wisla/', 'tabela.views.wisla', name='wisla'),
     url(r'^cracovia/', 'tabela.views.cracovia', name='cracovia'),
     url(r'^gornik_zabrze/', 'tabela.views.gornik_zabrze', name='gornik_zabrze'),
     url(r'^gornik_leczna/', 'tabela.views.gornik_leczna', name='gornik_leczna'),
     url(r'^podbeskidzie/', 'tabela.views.podbeskidzie', name='podbeskidzie'),
     url(r'^zaglebie/', 'tabela.views.zaglebie', name='zaglebie'),
     url(r'^piast/', 'tabela.views.piast', name='piast'),
     url(r'^ruch/', 'tabela.views.ruch', name='ruch'),
     url(r'^termalika/', 'tabela.views.termalika', name='termalika'),
     url(r'^korona/', 'tabela.views.korona', name='korona'),


    url(r'^admin/', include(admin.site.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)