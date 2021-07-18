from django.db import models

# Create your models here.
class CategoriaTrab(models.Model):
    nombre = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = "categoriaTrab"
        verbose_name_plural = "categoriasTrab"
    

    def __str__(self):
        return self.nombre


class Trabajos(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=300)
    imagen = models.ImageField(upload_to = 'trabajos', null = True, blank = True)
    categoria = models.ForeignKey(CategoriaTrab, on_delete = models.CASCADE)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = 'trabajo'
        verbose_name_plural = 'trabajos'
    
    def __str__(self):
        return self.nombre