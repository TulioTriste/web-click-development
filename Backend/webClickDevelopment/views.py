from django.shortcuts import render

# Create your views here.
def crud(request):
    usuarios = Usuario.objects.all()
    context = {
        'usuarios': usuarios,
    }
    return render(request, 'crud.html', context)