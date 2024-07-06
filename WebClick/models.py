from django.db import models

# Create your models here.
class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=12)
    correo = models.EmailField(max_length=100, unique=True, blank=True, null=True)
    password = models.CharField(max_length=30)
    activo = models.BooleanField()

    def __str__(self):
        return (
            str(self.nombre)
            + " "
            + str(self.apellido_paterno)
            + " "
            + str(self.apellido_materno)
        )

class Templates_Product(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=25)
    precio = models.IntegerField()
    imagen_url = models.CharField(max_length=300)
    descripcion = models.CharField(max_length=150)
    descuento = models.IntegerField()

    def __str__(self):
        return str(self.titulo) + " " + str(self.precio) + " " + str(self.descripcion)

class Carrito(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Templates_Product, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return (
            str(self.usuario)
            + " "
            + str(self.producto)
            + " "
            + str(self.cantidad)
            + " "
            + str(self.total)
        )

class Compra(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Templates_Product, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = models.IntegerField()
    fecha = models.DateField()

    def __str__(self):
        return (
            str(self.usuario)
            + " "
            + str(self.producto)
            + " "
            + str(self.cantidad)
            + " "
            + str(self.total)
        )
    
class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    # Añade más campos según sea necesario

    def __str__(self):
        return self.nombre