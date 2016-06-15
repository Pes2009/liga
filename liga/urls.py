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
     url(r'^create_club/', 'tabela.views.club_create', name='club_create'),
     url(r'^detail_club/(?P<id>\d+)/$', 'tabela.views.club_detail', name='club_detail'),


     # kluby
     url(r'^pogon/', 'tabela.views.pogon', name='pogon'),


    url(r'^admin/', include(admin.site.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)