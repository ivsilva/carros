from django import forms
from cars.models import Car, CarImage

class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

class CarImageForm(forms.ModelForm):
    class Meta:
        model = CarImage
        fields = ['image']  # Somente o campo de imagem
