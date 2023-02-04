from django.db import models

# Create your models here.
class Producto(models.Model):

    nombre=models.CharField(max_length=40)
    precio=models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Precio {self.precio}"

class Vendedor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - Email {self.email}"

class Cliente(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    localidad= models.CharField(max_length=30)
    
    
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Localidad {self.localidad}"

from django.contrib.auth.models import User

class Avatar(models.Model):

     user = models.ForeignKey(User, on_delete=models.CASCADE)
 
     imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

     def __str__(self):
         return f"{self.user} - {self.imagen}"


    

