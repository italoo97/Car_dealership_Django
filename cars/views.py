from django.shortcuts import render
from cars.models import Car

def cars_view(request):
	cars = Car.objects.filter() #(brand__name='Fiat') #aqui se usa 2 _ para indicar que voce quer pesquisar pelo nome e não pelo ID do item 
	
	return render(
				request, 
				'cars.html',
				{'cars': cars} #Aqui é um dicionario para simbolizar o banco de dados
				)