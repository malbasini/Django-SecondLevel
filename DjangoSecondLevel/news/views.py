from django.shortcuts import render
from django.http import HttpResponse
from .models import Articolo,Giornalista
# Create your views here.
#def home(request):
#   return HttpResponse('<h1> Homepage! </h1>')

def home(request):
    a = ""
    g = ""
    for art in Articolo.objects.all():
        a += (art.titolo +'<br>')
    for gio in Giornalista.objects.all():
        g += (gio.nome +'<br>')
    response = 'Articoli: <br>' + a + '<br> Giornalisti: <br>' + g
    return HttpResponse('<h1>' + response + '</h1>')