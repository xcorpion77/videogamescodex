"""
Definition of urls for Curso_Django.
"""

#from datetime import datetime
#import django.contrib.auth.views

from django.conf.urls import url
import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [

    url(r'^$', app.views.home),
    url(r'^videogame\/(?P<id>[0-9]+)$', app.views.ver_videogame),
    url(r'^borrar\/(?P<id>[0-9]+)$', app.views.borrar_videogame),
    url(r'^crear\/{0,1}$', app.views.crear_videogame),
    url(r'^ranking\/{0,1}$', app.views.ranking),
    url(r'^modificar\/(?P<id>[0-9]+)$', app.views.modificar_videogame),
    url(r'', app.views.not_found),

]
