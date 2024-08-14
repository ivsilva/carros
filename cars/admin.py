from django.contrib import admin
from cars.models import Car, Brand, CarImage, CarVideo  # Importando os modelos necessários

class BrandAdmin(admin.ModelAdmin):
    list_display = ('model',)
    search_fields = ['model',]

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1  # Permite adicionar uma nova imagem diretamente na página de admin do Carro

class CarVideoInline(admin.TabularInline):
    model = CarVideo
    extra = 1  # Permite adicionar um novo vídeo diretamente na página de admin do Carro

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ['model',]  # Defina os campos que serão pesquisáveis
    inlines = [CarImageInline, CarVideoInline]  # Adiciona as inlines de imagens e vídeos

# Registrando os modelos no admin
admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
