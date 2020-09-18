from django.db import models

# Create your models here.
class Horpakdetail(models.Model):
    name = models.CharField(max_length=100)
    water_bill =models.IntegerField()
    fire_bill =models.IntegerField()
    price =models.IntegerField()
    wifi = models.BooleanField(default=True)
    air = models.BooleanField(default=True)
    fan = models.BooleanField(default=True)
    typeMen = models.BooleanField(default=True)
    typeWomen =models.BooleanField(default=True)

    def __str__(self):
        return self.name

