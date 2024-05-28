from django.db import models


# Create your models here.
class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True, db_column="idGenero")
    genero = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self) -> str:
        return str(self.genero)
    
class Usuario(models.Model):
    rut = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=25)
    apellido_paterno = models.CharField(max_length=25)
    apellido_materno = models.CharField(max_length=25)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_genero = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column="idGenero")
    telefono = models.CharField(max_length=12)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.BooleanField()

    def __str__(self) -> str:
        return str(self.nombre) + " " + str(self.apellido_paterno) + " " + str(self.apellido_materno)