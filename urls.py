# -*- coding: utf-8 -*-
# czat/urls.py

from django.conf.urls import url
from . import views  # import widoków aplikacji

app_name = 'czat'  # przestrzeń nazw aplikacji
urlpatterns = [
    url(r'^$', views.index, name='index'),
]

from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^', include('czat.urls')),
    url(r'^admin/', admin.site.urls),
]
