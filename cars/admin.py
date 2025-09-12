from django.contrib import admin
from cars.models import Car, Brand

Modelo = 'model'
Marca = 'brand'
AnoFabricação = 'factory_year'
AnoModelo = 'model_year'
Plate = 'plate'
Valor = 'value'
Name = 'name'

class BrandAdmin (admin.ModelAdmin):
    list_display = (Name,)
    search_fields = (Name,)

class CarAdmin (admin.ModelAdmin):
    list_display = (Modelo, Marca, AnoFabricação, AnoModelo, Plate, Valor)
    search_fields = (Modelo, Marca)

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)