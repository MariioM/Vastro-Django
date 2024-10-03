from django.db import models
from django.urls import reverse

# Create your models here.
class MiningLocations(models.Model):
    name=models.CharField (
        unique=True,
        null=False,
        blank=False,
        max_length=50,
    )
    system=models.CharField(
        null=False,
        blank=False,
        max_length=50,
    )
    mineral=models.CharField(
        null=False,
        blank=False,
        max_length=50,
    )
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("location_detail", kwargs={"pk": self.pk})
    

class Ships(models.Model):
    class ShipSizes(models.TextChoices):
        XS = 'XS', 'Extra Small'
        S = 'S', 'Small'
        M = 'M', 'Medium'
        L = 'L', 'Large'
        XL = 'XL', 'Extra Large'
        SUB_CAPITAL = 'SC', 'Sub-Capital'
        CAPITAL = 'C', 'Capital'

    name=models.CharField (
        unique=True,
        null=False,
        blank=False,
        max_length=50,
    )
    ore_capacity=models.IntegerField(
        null=False,
        blank=False
    )
    crew_capacity=models.IntegerField(
        null=False,
        blank=False
    )
    destination=models.ForeignKey(
        MiningLocations,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='ships'
    )
    size = models.CharField(
        max_length=10,
        choices=ShipSizes.choices,
        null=False,
        blank=False
    )
    def __str__(self):
        return self.name