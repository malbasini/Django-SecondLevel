from django.urls import path
from news.views import home,articoloDetailView

urlpatterns = [
    path('', home , name='homeview'),
    path('articolo/<int:pk>', articoloDetailView , name='articoloDetail'),
]