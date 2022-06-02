from django.urls import path
from news.views import ArticoloDetailViewCB,ArticoloListView
from news.views import home

urlpatterns = [
    path('', home , name='homeview'),
    #path('articolo/<int:pk>', articoloDetailView , name='articoloDetail'),
    path('articolo/<int:pk>', ArticoloDetailViewCB.as_view() , name='articoloDetail'),
    path('listaarticoli/', ArticoloListView.as_view() , name='listaArticoli'),
]