from django.db import models

# Create your models here.
class Todo(models.Model):
    
    fecha_ingreso = models.DateTimeField(verbose_name="Fecha de ingreso")
    texto = models.CharField(verbose_name="Contenido del estado", max_length=230)

    class Meta:
        verbose_name = "To Do"
        verbose_name = "Estados"

    def __str__(self):
        return str(self.id) + ".- " + str(self.texto)
