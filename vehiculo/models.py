from django.core.validators import MinValueValidator
from django.db import models


class VehiculoModel(models.Model):
    MARCA_CHOICES = [
        ("CHEVROLET", "Chevrolet"),
        ("FIAT", "Fiat"),
        ("FORD", "Ford"),
        ("TOYOTA", "Toyota"),
    ]

    CATEGORIA_CHOICES = [
        ("PARTICULAR", "Particular"),
        ("TRANSPORTE", "Transporte"),
        ("CARGA", "Carga"),
    ]

    marca = models.CharField(
        max_length=20, choices=MARCA_CHOICES, default="FORD")
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(
        max_length=20, choices=CATEGORIA_CHOICES, default="PARTICULAR")
    precio = models.IntegerField(validators=[MinValueValidator(0)])
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # timestamp
    fecha_modificacion = models.DateTimeField(auto_now=True)  # updated

    class Meta:
        permissions = [
            ("visualizar_catalogo", "Puede visualizar catalogo"),
            # ("add_vehiculomodel", "Can add vehiculo model"),
        ]
        verbose_name_plural = "Vehículos"
        ordering = ["-fecha_creacion"]

    def __str__(self):
        return self.marca
