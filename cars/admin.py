from django.contrib import admin
from cars.models import Car, Brand, CarImage  # Importar CarImage

# Admin para Brand
class BrandAdmin(admin.ModelAdmin):
    list_display = ('model',)
    search_fields = ['model']

# Admin para CarImage (opcional, se você deseja gerenciar imagens diretamente pelo admin)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ('car', 'image')
    search_fields = ['car__model']  # Permite buscar imagens por modelo do carro

# Admin para Car com inline para CarImage
class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1  # Número de formulários em branco a serem exibidos inicialmente

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ['model']
    inlines = [CarImageInline]  # Adiciona o inline para imagens no admin de Car

# Registro dos modelos no admin
admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(CarImage, CarImageAdmin)  # Opcional, se você deseja acessar CarImage diretamente
