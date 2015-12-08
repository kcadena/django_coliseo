from django.shortcuts import render,render_to_response,RequestContext,redirect
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from django.utils import timezone

from .forms import MyModel
from .forms import ModelPersona,ModelCampeonato,ModelEquipo,ModelJugador,ModelPartido,ModelPartidoAnotacion,ModelPartidoArbitro

# Create your views here.

class IndexView(TemplateView):
	template_name='index.html'


def Personas(request):

    if request.method == "POST":
        form = ModelPersona(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            #model_instance.timestamp = timezone.now()
            model_instance.save()
            return HttpResponseRedirect("personas")
            
    else:
        form = ModelPersona()

    return render(request, "fPersona.html", {'form': form})

def Campeonato(request):

    if request.method == "POST":
        form = ModelCampeonato(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            #model_instance.timestamp = timezone.now()
            model_instance.save()
            return HttpResponseRedirect("campeonatos")
    else:
        form = ModelCampeonato()

    return render(request, "fCampeonato.html", {'form': form})

def Equipo(request):

    if request.method == "POST":
        form = ModelEquipo(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            #model_instance.timestamp = timezone.now()
            model_instance.save()
            return HttpResponseRedirect("equipos")
    else:
        form = ModelEquipo()

    return render(request, "fEquipos.html", {'form': form})

def Jugador(request):

    if request.method == "POST":
        form = ModelJugador(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            #model_instance.timestamp = timezone.now()
            model_instance.save()
            return HttpResponseRedirect("jugadores")
            
    else:
        form = ModelJugador()

    return render(request, "fjugador.html", {'form': form})


def Partido(request):

    if request.method == "POST":
        form = ModelPartido(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            #model_instance.timestamp = timezone.now()
            model_instance.save()
            return HttpResponseRedirect("partidos")
            
    else:
        form = ModelPartido()

    return render(request, "fPartidos.html", {'form': form})


def PartidoAnotacion(request):

    if request.method == "POST":
        form = ModelPartidoAnotacion(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            #model_instance.timestamp = timezone.now()
            model_instance.save()
            return HttpResponseRedirect("partidos_anotaciones")
            
    else:
        form = ModelPartidoAnotacion()

    return render(request, "fPartidoAnotacion.html", {'form': form})


def PartidoArbitro(request):

    if request.method == "POST":
        form = ModelPartidoArbitro(request.POST)
        if form.is_valid():

            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            #model_instance.timestamp = timezone.now()
            model_instance.save()
            return HttpResponseRedirect("partidos_arbitros")
             
    else:
        form = ModelPartidoArbitro()

    return render(request, "fArbitroPartido.html", {'form': form})


