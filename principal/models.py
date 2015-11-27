from django.db import models
from django.utils import timezone
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

# Create your models here.
class Instrumento(models.Model):
    autor = models.ForeignKey('auth.User', null = True, blank=True)
    nombre = models.CharField("Nombre", max_length=100)
    marca= models.CharField("Marca", max_length=100)
    categoria= models.ForeignKey('Categoria')
    precio = models.DecimalField("Precio", max_digits=8, decimal_places=2)
    descripcion = models.TextField("Descripcion")
    imagen_instrumento= models.ImageField("Imagen", upload_to="images/", blank=True, null=True)
    fecha_creacion = models.DateTimeField("Fecha de creacion", default=timezone.now)
    fecha_publicacion = models.DateTimeField("Fecha de publicacion", blank=True, null=True)
    

    def __str__(self):
        return self.nombre
 
@receiver(pre_delete, sender=Instrumento)
def post_pre_delete_handler(sender, instance, **kwargs):
    instance.imagen_instrumento.delete(False)

    def publicar(self):
        self.fecha_publicacion= timezone.now()
        self.save()

class Categoria(models.Model):
    nombre=models.CharField("Nombre categoria", max_length=100)
    descripcion= models.TextField("Descripcion categoria")

    def __str__(self):
        return self.nombre


