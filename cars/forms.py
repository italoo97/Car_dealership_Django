from django import forms
from cars.models import Brand, Car

# class CarForm(forms.Form):
#     model = forms.CharField(max_length=200) #models.CharField(max_length=200, blank=False, null=False)
#     brand = forms.ModelChoiceField(Brand.objects.all()) #models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
#     factory_year = forms.CharField() #models.CharField(max_length=4, choices=get_year_choices(), default=str(datetime.now().year))
#     model_year = forms.CharField() #models.CharField(max_length=4, choices=get_year_choices(), default=str(datetime.now().year))
#     plate = forms.CharField(max_length=10) #models.CharField(max_length=10, blank=True, null=True)
#     value = forms.FloatField() #models.FloatField(blank=True, null=True)
#     photo = forms.ImageField() #models.ImageField(upload_to='cars/', blank=True, null=True)

#     def save(self):
#         car = Car(
#             model = self.cleaned_data['model'],
#             brand = self.cleaned_data['brand'],
#             factory_year = self.cleaned_data['factory_year'],
#             model_year = self.cleaned_data['model_year'],
#             plate = self.cleaned_data['plate'],
#             value = self.cleaned_data['value'],
#             photo = self.cleaned_data['photo'],
#         )
#         car.save()
#         return car
    
class CarModelForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor Minimo deve ser de R$20.000')
        return value