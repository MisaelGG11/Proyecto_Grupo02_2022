#============================#
# DJANGO VERSION: 3.2.15 LTS #
#============================#

from django.db import models

class Trabajador():
    nombres = models.CharField(max_length=120, default='nombre')
    apellidos = models.CharField(max_length=120, default='apellidos')

class Cliente(models.Model):
    nombres = models.CharField(max_length=120, default='nombres')
    apellidos = models.CharField(max_length=120, default='apellidos')

class Catalogo_Orden(models.Model):
    nombre = models.CharField(max_length=20, default='Nada')

class Orden(models.Model):
    #Fecha
    fecha_recepcion = models.DateField(default='0-0-0')
    fecha_entrega =  models.DateField(default='0-0-0')
    #Camisa
    talla = models.CharField(null=True, default='Nada')
    manga = models.CharField(null=True, default='Nada')
    pecho = models.CharField(null=True, default='Nada')
    ancho = models.CharField(null=True, default='Nada')
    hombros = models.CharField(null=True, default='Nada')
    largo_camisa = models.CharField(null=True, default='Nada')
    #Pantalon
    largo_pantalon = models.CharField(null=True, default='Nada')
    cintura = models.CharField(null=True, default='Nada')
    cadera = models.CharField(null=True, default='Nada')
    #Llaves foraneas -> catalogo_orden(tipo de orden), cliente, encargado
    tipo_orden = models.ForeignKey(Catalogo_Orden, on_delete=models.DO_NOTHING)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.DO_NOTHING)

class Medida():
    nombre = models.CharField()

# La creacion de roles, se derivaran 
# de la clase principal Users; 
# implementacion parcial
class Usuario(models.Model):
    def getRet():
        return None