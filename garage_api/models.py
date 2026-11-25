from django.db import models

class Manufacture(models.Model):
    name = models.CharField(
        max_length=100,
    )

    country = models.CharField(
        max_length=100,
    )

    found_year = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

class Car(models.Model):
    model = models.CharField(
        max_length=100,
    )

    year = models.PositiveSmallIntegerField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    manufacture = models.ForeignKey(
        to=Manufacture,
        on_delete=models.CASCADE,
        related_name='cars',
    )