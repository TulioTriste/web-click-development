from django.shortcuts import render
from .models import Usuario,Templates_Product
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context = {
        "user": "",
        "templates": get_templates()
    }
    return render(request, 'pages/index.html', context)

def register(request):
    return render(request, 'pages/register.html')

def about_page(request):
    return render(request, 'pages/about.html')

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

def loginSession(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username=="seb.moralesf" and password=="pass1234":
            request.session["user"] = username
            usuarios = Usuario.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"pages/index.html",context)
        else:
            context = {
                "mensaje":"Usuario o contraseña incorrecta",
                "design":"alert alert-danger w-50 mx-auto text-center",
            }
            return render(request,"registration/login.html",context)
    else:
        context = {

        }
        return render(request,"registration/login.html",context)

def conectar(request):
    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            usuarios = Usuario.objects.all()
            context = {
                "usuarios":usuarios,
            }
            return render(request,"pages/index.html",context)
        else:
            context = {
                "mensaje":"Usuario o contraseña incorrecta",
                "design":"alert alert-danger w-50 mx-auto text-center",
            }
            return render(request,"registration/login.html",context)
    else:
        context = {

        }
        return render(request,"registration/login.html",context)

@login_required
def desconectar(request):   
    if request.user.is_authenticated:
        logout(request)
    
    context = {
        "mensaje":"Desconectado con exito",
        "design":"alert alert-success w-50 mx-auto text-center",
    }
    return render(request,"registration/login.html",context)

def templates(request):
    context = {
        "templates": get_templates()
    }

    return render(request,"pages/templates_page.html",context)

def get_templates():
    productos_templates = Templates_Product.objects.all()

    for templ in productos_templates:
        if templ.descuento != 0:
            templ.precio = templ.precio - (templ.precio * templ.descuento)
            
    return productos_templates

def get_templates_without_modify():
    productos_templates = Templates_Product.objects.all()
            
    return productos_templates

def template(request, pk):
    template = Templates_Product.objects.get(id=pk)
    context = {
        "template": template
    }
    return render(request, "pages/template.html", context)

@login_required
def carrito(request):
    return render(request, "pages/carrito.html")

@login_required
def panel(request):
    context = {
        "templates": get_templates_without_modify()
    }
    return render(request, "pages/panel.html", context)

@login_required
def template_add(request):
    return render(request, "pages/template_add.html")

@login_required
def add_template(request):
    if request.method != "POST":
        usuarios = Templates_Product.objects.all()
        context = {
            "templates": usuarios
        }
        return render(request, "pages/template_add.html", context)
    else:
        titulo = request.POST["titulo"]
        precio = request.POST["precio"]
        imagen_url = request.POST["imagen_url"]
        descripcion = request.POST["descripcion"]
        descuento = request.POST["descuento"]

        if descuento == "":
            descuento = 0

        obj = Templates_Product.objects.create(
            titulo=titulo,
            precio=precio,
            imagen_url=imagen_url,
            descripcion=descripcion,
            descuento=descuento,
        )
        obj.save()
        context = {
            "mensaje": "Registro Exitoso",
        }
        return render(request, "pages/template_add.html", context)

@login_required
def remove_template(request, pk):
    try:
        template = Templates_Product.objects.get(id=pk)
        template.delete()

        templates = get_templates_without_modify()
        context = {
            "mensaje": "Template Eliminado Correctamente",
            "templates": templates,
        }
        return render(request, "pages/panel.html", context)
    except:
        templates = get_templates_without_modify
        context = {
            "mensaje": "Error, ID no Encontrado...",
            "templates": templates,
        }
        return render(request, "pages/panel.html", context)