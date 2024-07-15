from django.db import models

# Create your models here.

class Zapatilla(models.Model):
    id_zapatilla = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='imagenes_zapatillas/')

    def __str__(self):
        return self.nombre