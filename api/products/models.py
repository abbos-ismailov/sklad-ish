from django.db import models
from api.base.models import BaseModel
# Create your models here.

class Xomashyo(BaseModel):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

class Mahsulot(BaseModel):
    name = models.CharField(max_length=250)
    kodi = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name


class XomashyoMahsulot(BaseModel):
    mahsulot_id = models.ForeignKey(Mahsulot, on_delete=models.CASCADE, related_name="mahsulot")
    xomashyo_id = models.ForeignKey(Xomashyo, on_delete=models.CASCADE, related_name="xomashyo")
    quantity = models.FloatField()


class Store(BaseModel):
    xomashyo_id = models.ForeignKey(Xomashyo, on_delete=models.CASCADE, related_name="xomashyo_store")
    remainder = models.PositiveIntegerField()
    price = models.FloatField()

