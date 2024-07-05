from django.contrib import admin
from .models import Usuario,Templates_Product, Carrito, Compra

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Templates_Product)
admin.site.register(Carrito)
admin.site.register(Compra)
