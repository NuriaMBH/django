

from django.urls import path
from hospitales import views

urlpatterns = [
    path('', views.index,name='index'),
    path('departamentos/', views.departamentosBBDD,name='departamentos'),
    path('hospitales/', views.hospitalesBBDD,name='hospitales'),
    path('insertardept/', views.insertarDepartamento,name='insertardept'),
    path('deletedept/', views.deleteDepartamento,name='deletedept'),
    
    
]                           