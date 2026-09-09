from django.db import models
from django.contrib.auth.models import User


class programador(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    esta_activo = models.BooleanField(default=True)


class Animal(models.Model):
    ESTADO_DISPONIBLE = "Disponible"
    ESTADO_ADOPTADO = "Adoptado"
    ESTADO_BAJA = "Dado de baja"

    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    raza = models.CharField(max_length=100)
    sexo = models.CharField(max_length=20)
    tamanio = models.CharField(max_length=50)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='imagenes/dogs/')
    estado = models.CharField(max_length=50, default=ESTADO_DISPONIBLE)

    # Las publicaciones históricas del proyecto fueron cargadas con fechas
    # ficticias de demostración; las nuevas reciben la fecha automáticamente.
    fecha_publicacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    fecha_adopcion = models.DateTimeField(null=True, blank=True)
    fecha_baja = models.DateTimeField(null=True, blank=True)

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nombre
