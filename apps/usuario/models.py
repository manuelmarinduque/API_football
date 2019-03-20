from django.db import models
import datetime


# Create your models here.
class Usuario(models.Model):

    generos = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )

    cedula = models.CharField(max_length=12,primary_key=True)
    nombre_usuario = models.CharField(max_length=20)
    password = models.CharField(max_length=12)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    sexo = models.CharField(max_length=1, choices=generos)
    correo = models.EmailField()
    saldo = models.PositiveIntegerField()
    telefono = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=30)

    def getedad(self):
        return int((datetime.date.today() - self.fecha_nacimiento).days / 365.25)


