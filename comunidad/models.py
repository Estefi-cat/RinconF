from django.db import models

# Create your models here.
class Leyend(models.Model):
    title = models.CharField(max_length=200, verbose_name= "Título" )
    description = models.TextField(verbose_name= "Descripción")
    image = models.ImageField(verbose_name= "Imagen", upload_to="leyends")
    created = models.DateTimeField(auto_now_add=True, verbose_name= "Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name= "Fecha de modificación")

    def __str__(self) :
        return self.title

    class Meta:
        verbose_name = "leyenda"
        verbose_name_plural = "leyendas"
        ordering = ["-created"]