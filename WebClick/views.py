from django.shortcuts import render
from .models import Usuario
from .forms import UsuarioForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    usuario=request.session["username"]
    context = {'usuario', usuario}
    return render(request, 'pages/index.html', context)

def register(request):
    return render(request, 'pages/register.html')

def user_add(request):
    if request.method != "POST":
        usuarios = Usuario.objects.all()
        context = {
            "usuarios": usuarios
        }
        return render(request, "pages/register.html", context)
    else:
        rut = request.POST["rut"]
        nombre = request.POST["nombre"]
        appPaterno = request.POST["appPaterno"]
        appMaterno = request.POST["appMaterno"]
        fechaNac = request.POST["fecha"]
        telefono = request.POST["telefono"]
        correo = request.POST["correo"]
        password = request.POST["password"]
        activo = True

        obj = Usuario.objects.create(
            rut=rut,
            nombre=nombre,
            apellido_paterno=appPaterno,
            apellido_materno=appMaterno,
            fecha_nacimiento=fechaNac,
            telefono=telefono,
            correo=correo,
            password=password,
            activo=activo,
        )
        obj.save()
        context = {
            "mensaje": "Registro Exitoso",
        }
        return render(request, "pages/register.html", context)