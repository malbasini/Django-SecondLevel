from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Articolo,Giornalista
# Create your views here.
def home(request):
    articoli = Articolo.objects.all()
    giornalisti = Giornalista.objects.all()
    context={'articoli':articoli,'giornalisti':giornalisti}
    return render(request,'homepage.html',context)

def articoloDetailView(request,pk):
    #articolo = Articolo.objects.get(pk=pk)
    #get_object_or_404 restituisce l'articolo se
    #esiste o una schermata con codice 404 (not found)
    #se l'articolo non esiste. Decisamente meglio
    #di una schermata di errore.
    articolo = get_object_or_404(Articolo,pk=pk)
    context={'articolo':articolo}
    return render(request,'articoloDetail.html',context)

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class ArticoloDetailViewCB(DetailView):
    model = Articolo
    template_name = 'articoloDetail.html'
    
class ArticoloListView(ListView):
    model = Articolo
    template_name = 'listaArticoli.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articoli'] = Articolo.objects.all()
        return context