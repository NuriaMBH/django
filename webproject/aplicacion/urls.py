from django.urls import path
from aplicacion import views
# lo que quiero que el usuario escriba
urlpatterns=[
    path('',views.index, name='index'),
    path('viernes/',views.metodoviernes, name='viernes')
]
#http://127.0.0.1:8000/ tengo que poner viernes/
