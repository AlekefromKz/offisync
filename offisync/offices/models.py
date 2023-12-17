from cities_light.models import City
from django.db import models


class Office(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    latitude = models.DecimalField(
        max_digits=8, decimal_places=5, null=True, blank=True
    )

    longitude = models.DecimalField(
        max_digits=8, decimal_places=5, null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Office"
        verbose_name_plural = "Offices"
