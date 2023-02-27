from django.shortcuts import render, redirect
import requests


def index_page(request):
	return render(request, 'index.html')

def get_weather_data(message):
	key = '45c45273f4bd8f87117b603a7dc03b5d'
	request_link = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + key
	
	city = str(message)

	response = requests.get(request_link.format(city)).json()

	city_info = {
		'city': city.upper()[0] + city[1:],
		'temp': response["main"]["temp"],
		'pressure': response["main"]["pressure"]*0.75,
		'humidity': response["main"]["humidity"],
		'icon': response["weather"][0]["icon"]
	}
	return city_info

def find_weather_in_city(request):
	message = request.GET['message']

	key = '45c45273f4bd8f87117b603a7dc03b5d'
	request_link = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + key
	city = str(message)

	resp = requests.get(request_link.format(city)) 

	if resp.status_code == 200:
		return render(request, 'weathercity.html', get_weather_data(message))
	else:
		data = {'key1': f'города {city} не существует', 'key2': 'повторно'}
		return render(request, 'index.html', data)
	