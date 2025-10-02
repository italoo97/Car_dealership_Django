from django.shortcuts import render, redirect
from cars.models import Car
from cars.forms import CarModelForm

def cars_view(request):
	cars = Car.objects.all().order_by('model')
	search = request.GET.get('search')
	
	if search:
		cars = Car.objects.filter(model__icontains=search) #(brand__name='Fiat') #aqui se usa 2 _ para indicar que voce quer pesquisar pelo nome e não pelo ID do item 
										# o icontains ele ignora letras maiusculas e minusculas trazendo todos os dados 

	return render(
				request, 
				'cars.html',
				{'cars': cars} #Aqui é um dicionario para simbolizar o banco de dados
				)

def new_cars_view(request):
	if request.method =='POST':
		new_car_form = CarModelForm(request.POST, request.FILES)
		if new_car_form.is_valid():
			new_car_form.save()
			return redirect('cars_list')
	else:
		new_car_form = CarModelForm()
	return render(request, 'new_car.html', {'new_car_form': new_car_form})