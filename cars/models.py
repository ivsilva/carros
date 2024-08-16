from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    
    def __str__(self):
        return self.model

class Car(models.Model):
    id = models.AutoField(primary_key=True)                                                                 
    model = models.CharField(max_length=200)                                    
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year =  models.IntegerField(blank=True, null=True) 
    plate = models.CharField(max_length=210, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.model

class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_images/')
    
    def __str__(self):
        return f'Image for {self.car.model}'

class CarInventario(models.Model):
    cars_count = models.IntegerField() # Quantidade de carros em estoque
    cars_value = models.FloatField() # Valor total de carros em nosso estoque
    created_at = models.DateField(auto_now_add=True) # Armazena data e horário. auto_now_add o django alimenta automaticamente com a data atual

    class Meta: # Sobre escrevendo minha class Meta
        ordering = ['-created_at'] # Ordenando do mais recente para mais antigo

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}' # Print
