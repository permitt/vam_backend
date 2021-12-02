from django.db import models

# Create your models here.
from address.models.country_model import Country


class Address(models.Model):
    street = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
