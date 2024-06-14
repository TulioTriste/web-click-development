from .models import Usuario

from django.forms import ModelForm

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"