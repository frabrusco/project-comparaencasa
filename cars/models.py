from django.db import models

# Create your models here.

class Car(models.Model):

    id = models.AutoField(primary_key=True)
    car_plate = models.CharField(max_length=50, unique=True)
    car_name = models.CharField(max_length=50)

    class Meta:
        ordering = ('car_name',)
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self):
        return f'{self.car_plate}-{self.car_name}'
