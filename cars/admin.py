from django.contrib import admin
from cars.models import Car

Modelo = 'model'
Marca = 'brand'
AnoFabricação = 'factory_year'
AnoModelo = 'model_year'
Valor = 'value'

class CarAdmin (admin.ModelAdmin):
    list_display = (Modelo, Marca, AnoFabricação, AnoModelo, Valor)
    search_fields = (Modelo, Marca)

admin.site.register(Car, CarAdmin)