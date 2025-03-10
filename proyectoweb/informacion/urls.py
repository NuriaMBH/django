from django.urls import path
from informacion import views

urlpatterns= [
    path ('',views.index, name='index'),
    path ('pelis/',views.pelis, name='pelis'),
    path ('futbol/',views.futbol, name='futbol'),
    path ('jugadoresl/',views.jugadores, name='jugadores') 
]