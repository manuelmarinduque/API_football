from django.db import models



# Create your models here.

class Apuesta(models.Model):
	idApuesta = models.CharField(primary_key=True, max_length=100)
	tipo =  models.CharField(max_length=100)
	fechaApuesta = models.DateField(auto_now=True)
	montoApuesta = models.PositiveIntegerField(default=0)
	gano = models.BooleanField(default=False)
	valorganado = models.PositiveIntegerField(default=0)
	nombreEquipo = models.CharField(max_length=100)
	idPartido = models.PositiveIntegerField(default=0)
	golesLocal = models.PositiveIntegerField(default=0)
	golesVistante = models.PositiveIntegerField(default=0)
	diferenciaGoles = models.PositiveIntegerField(default=0)
	cedula = models.ForeignKey('usuario.Usuario', on_delete=models.CASCADE)