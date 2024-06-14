from django.shortcuts import render
from .models import Usuario
from .forms import UsuarioForm

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')

def user_add(request):
    rut = request.POST["rut"]
    nombre = request.POST["nombre"]
    appPaterno = request.POST["appPaterno"]
    appMaterno = request.POST["appMaterno"]
    fechaNac = request.POST["fecha"]
    telefono = request.POST["telefono"]
    correo = request.POST["correo"]
    password = request.POST["password"]
    direccion = request.POST["direccion"]
    activo = True

    obj = Usuario.objects.create(
        rut=rut,
        nombre=nombre,
        apellido_paterno=appPaterno,
        apellido_materno=appMaterno,
        fecha_nacimiento=fechaNac,
        telefono=telefono,
        email=correo,
        password=password,
        direccion=direccion,
        activo=activo,
    )
    obj.save()
    context = {
        "mensaje": "Registro Exitoso",
    }
    return render(request, "pages/register.html", context)