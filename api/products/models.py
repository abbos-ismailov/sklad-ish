from django.db import models
from api.base.models import BaseModel
# Create your models here.

class Material(BaseModel):
    name = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

class Product(BaseModel):
    name = models.CharField(max_length=250)
    code = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.name


class MaterialProduct(BaseModel):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="mahsulot")
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="xomashyo")
    quantity = models.FloatField()


class Store(BaseModel):
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="xomashyo_store")
    remainder = models.PositiveIntegerField()
    price = models.FloatField()

