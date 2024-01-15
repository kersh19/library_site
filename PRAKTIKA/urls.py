from django.urls import re_path,include
from django.contrib.messages import success
from django.urls import path
from PRAKTIKA import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
urlpatterns= [
    re_path(r'^$', views.base, name='base'),
    re_path(r'^abil/$', views.base_abi, name='abil'),
    re_path(r'^biblioteka/$', views.o_bibl, name='biblioteka'),
    re_path(r'^exhibitions/$', views.exhibition, name='exhibitions'),
    re_path(r'^kontakt/$', views.kontakt, name='kontakt'),
    re_path(r'^prepod/$', views.prep, name='prepod'),
    re_path(r'^student/$', views.student, name='student'),
    re_path(r'^Dates/$', views.date, name='Date'),
    re_path(r'^historypr/$', views.historypr, name='historypr'),
    re_path(r'^historynas/$', views.historynas, name='historynas'),
    re_path(r'^Dates/(?P<date_id>[0-9]+)/$', views.date, name='Dates'),
    re_path(r'^polozhenia/$', views.polozh, name='polozhenia'),
    re_path(r'^nov_iz/$', views.nov_iz, name='nov_iz'),
]
if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)