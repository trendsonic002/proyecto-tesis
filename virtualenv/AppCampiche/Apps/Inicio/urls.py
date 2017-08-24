from django.conf.urls import url,include
from django.contrib import admin
from Apps.Inicio.views import iniciar_sesion

urlpatterns = [
    url(r'^$',iniciar_sesion,name='iniciar_sesion'),
]