from django.db import models
from enum import Enum
from .storage import OverwriteStorage

class Modules(Enum):
    CAJONERA = "CAJONERAS"
    COLGADOR = "COLGADORES"
    REPISERO = "REPISEROS"


class ModulesPrice(models.Model):
    price = models.FloatField(default=0)
    typeOf = models.CharField(
        max_length=20,
        choices=[("CAJONERA","Cajonera"),
                 ("COLGADOR","Colgador"),
                 ("REPISERO","Repisero"),
                 ]  # Choices is a list of Tuple
    )
    size = models.FloatField(default=0)
    door = models.BooleanField(default=False)
    interiorBlanco = models.BooleanField(default=False)


class Textures(models.Model):
    space = models.FloatField(default=0)
    name = models.CharField(default="NONE", max_length=100)
    img = models.ImageField(upload_to='Textures', max_length=9999, storage=OverwriteStorage())
