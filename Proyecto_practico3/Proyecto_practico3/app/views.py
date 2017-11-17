#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime

from app.models import Videogames
from app.forms import VideogameForm


def home(request):
    videogames = Videogames.objects.order_by('name')
    return render(
        request,
        'app/index.html',
        {
            "title" : "Inicio",
            "videogames" : videogames,
        }
    )

def ranking(request):
    videogames = Videogames.objects.order_by('-score')
    return render(
        request,
        'app/ranking.html',
        {
            "title" : "Ranking",
            "videogames" : videogames,
        }
    )

def ver_videogame(request, id):
    videogame = Videogames.objects.get(pk=id)
    return render(request,
                 'app/ver_videogame.html',
                 { "videogame" : videogame }
                 )

def crear_videogame(request):
    if request.method == 'POST':

        # Formulario rellenado, guardarlo
        formulario = VideogameForm(request.POST)
        if formulario.is_valid():
            #guardamos el formulario
            videogame = formulario.save()
            return HttpResponseRedirect('/videogame/' + str(videogame.id))

    elif request.method == 'GET':
        # Peticion de formulario, mandar uno
        formulario = VideogameForm()
        return render(request,
                    'app/videogame_form.html',
                    { 'form' : formulario,
                      'action': "/crear"}
                    )
    else:
        return render(request, 'app/404.html')

def modificar_videogame(request, id):

    videogame = Videogames.objects.get(pk=id)
    if request.method == 'POST':
        formulario = VideogameForm(request.POST, instance=videogame)
        if formulario.is_valid():
            videogame = formulario.save()
            return HttpResponseRedirect("/videogame/" + str(videogame.id))

    elif request.method == 'GET':
        formulario = VideogameForm(instance = videogame)
        return render(request,
                      'app/videogame_form.html',
                      {'form': formulario,
                       'action' : '/modificar/' + str(videogame.id)}
                      )
    else:
        return render(request, 'app/404.html')


def get_genre_display(indice):
    genre = ""
    for tupla in Videogames.GENRES:
        if indice == tupla[0]:
            genre = tupla[1]
            break
    return genre

def borrar_videogame(request, id):
    videogame = Videogames.objects.get(pk=id)
    videogame.delete()
    return HttpResponseRedirect('/') 

def not_found(request):
    return render(request, 'app/404.html')