from django.contrib import admin
from cars.models import Car, Brand #Da pasta cars do arquivo models importar cars


class BrandAdmin(admin.ModelAdmin):
    list_display = ('model',)
    search_fields = ['model',]

class CarAdmin(admin.ModelAdmin):
    list_display = ('model','brand','factory_year','model_year','value')
    search_fields = ['model',] #Defina quais nomes quer buscar

admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)


