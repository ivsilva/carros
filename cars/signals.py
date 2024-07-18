from django.db.models.signals import post_delete, post_save, pre_save
from cars.models import Car, CarInventario
from django.dispatch import receiver
from django.db.models import Sum

# Update de inventario
def Car_Inventario_Update(): 
    cars_count = Car.objects.all().count()  # Corrigido: adicionado parênteses
    cars_value = Car.objects.aggregate(total_value=Sum('value'))['total_value'] 

    CarInventario.objects.create(
        cars_count=cars_count, 
        cars_value=cars_value
    ) 

@receiver(pre_save, sender=Car) # Adicionando texto antes de salvar no meu banco de dados
def car_pre_save(sender, instance, **kwargs):
    if not instance.bio:  # se não tem descrição
        instance.bio = 'Bio Gerada Automaticamente'  # Então adicione

@receiver(post_save, sender=Car) # Salvando carro no estoque
def Car_PostSave(sender, instance, **kwargs):
    Car_Inventario_Update()
    
@receiver(post_delete, sender=Car) # Deletando carro de estoque
def Car_Post_delete(sender, instance, **kwargs):
    Car_Inventario_Update()
