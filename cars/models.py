from django.db import models
from datetime import datetime

def get_year_choices():
    current_year = datetime.now().year
    return [(str(ano), str(ano)) for ano in range(current_year + 1, current_year - 100, -1)]

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200, blank=False, null=False)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.CharField(max_length=4, choices=get_year_choices(), default=str(datetime.now().year))
    model_year = models.CharField(max_length=4, choices=get_year_choices(), default=str(datetime.now().year))
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)

    def __str__(self):
        return self.model