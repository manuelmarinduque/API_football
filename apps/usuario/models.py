from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Usuario(User, models.Model):

    generos = (
        ('M', 'Masculino'),
        ('F', 'Femenino')
    )

    cedula = models.CharField(max_length=12, primary_key=True)
    sexo = models.CharField(max_length=1, choices=generos)
    saldo = models.PositiveIntegerField(default=0)
    telefono = models.CharField(max_length=10)
    fecha_nacimiento = models.DateField()
    pais = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=30)
