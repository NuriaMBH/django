from django.shortcuts import render
from hospitales.models import ServiceDepartamento, ServiceHospital

# Create your views here.
def index(request):
    return render(request,'pages/index.html')
def departamentosBBDD(request):
    servicio = ServiceDepartamento()
    departamentos = servicio.getDepartamentos()
    #para enviar el menu departamentos a la pagina
    context = {
        "departamentos":departamentos
    }
    return render(request,'pages/departamentos.html',context)

def hospitalesBBDD(request):
    servicio = ServiceHospital()
    hospitales = servicio.getHospitales()
    #para enviar el menu departamentos a la pagina
    context = {
        "hospitales":hospitales
    }
    return render(request,'pages/hospitales.html',context)

def insertarDepartamento(request):
    if('cajanumero' in request.POST):
        servicio= ServiceDepartamento()
        numero = request.POST['cajanumero']
        nombre = request.POST['cajanombre']
        localidad = request.POST['cajalocalidad']
        registros= servicio.insertDepartamento(numero,nombre,localidad)
        departamentos = servicio.getDepartamentos()
        context= {
            "departamentos": departamentos
               }   
    
        return render(request,'pages/departamentos.html', context)
    else:
        return render(request,'pages/insertardepartamento.html')
   ############ 
def deleteDepartamento(request):
    servicio = ServiceDepartamento()
    departamentos = servicio.getDepartamentos()
    
    context = {
        "departamentos":departamentos
    }
    return render(request,'pages/deletedepartamento.html',context)
    
    
    
