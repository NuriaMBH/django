from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'informacion/index.html')

def pelis(request):
    return render(request,'informacion/pelis.html')

def futbol(request):
    nombre = "Real Madrid"
    data = {
        "equipo": nombre
    }
    return render(request,'informacion/futbol.html',data)

def jugadores(request):
    listaJugadores=[
        { "Nombre":"Cristiano Ronaldo",
        "Demarcacion":"Delantero",
        "Numero": 7 },
        { "Nombre": "Guti",
        "Demarcacion": "Centrocampista",
        "Numero": 14 },
        { "Nombre": "Karim Benzema",
        "Demarcacion": "Delantero",
        "Numero":9 },
        { "Nombre": "Toni Kroos",
        "Demarcacion": "Centrocampista",
        "Numero":8 },
        {"Nombre": "Thibaut Courtois",
        "Demarcacion": "Portero",
        "Numero": 1}
        
    ]
    context = {
        "jugadores":listaJugadores
    }
    return render(request,'informacion/jugadores.html',context)
def colores(request):
    #RECUPERAMOS LA VARIABLE QUE NOS ESTAN ENVIANDO
    #MEDIANTES GET(micolor)
    #DEBEMOS COMPROBAR QUE RECIBIMOS ALGO LLAMADO micolor
        if('micolor' in request.GET):
            colorRecibido= request.GET['micolor']
            context = {
            "colordibujo":colorRecibido
        }
        
            return render(request,'informacion/colores.html',context)
        else:
        
            return render(request,'informacion/colores.html')
 
def saludo(request):
    #debemos preguntarle si hemos recibido datos del formulario
    if ('cajanombre' in request.POST):
        nombreRecibido = request.POST['cajanombre']
        context = {
            "nombre": nombreRecibido
        }
    else:
        return render(request,'informacion/saludo.html')
def sumarNumeros(request):
    if('cajanumero1' in request.POST):
        num1 = request.POST['cajanumero1']
        num2 = request.POST['cajanumero2']
        suma = int(num1) + int(num2)
        context = {
            "suma": suma,
            "numero1":num1,
            "numero2":num2
        }
        return render(request, "informacion/sumarnumeros.html",context)    
    else:
        return render(request, "informacion/sumarnumeros.html")
    
def collatz(request):
    return render(request, "informacion/collatz.html")
    
    