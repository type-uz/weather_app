from django.shortcuts import render
import requests
from datetime import datetime


def index(request):
    try:
        city_weather_updates = []

        if request.method == 'POST':
            API_KEY = '4400a29856d8ecf9ea937573a62f7e73'
            cities = request.POST.getlist('city')

            for city_name in cities:
                url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric'
                response = requests.get(url).json()
                current_time = datetime.now()
                formatted_time = current_time.strftime("%Y, %B, %d, %A")
                city_weather_update = {
                    'city': city_name,
                    'description': response['weather'][0]['description'],
                    'icon': response['weather'][0]['icon'],
                    'temperature': 'Temperature: ' + str(response['main']['temp']) + ' °C',
                    # 'max_temperature': 'Max Temperature: ' + str(response['main']['temp_max']) + ' °C',
                    # 'min_temperature': 'Min Temperature: ' + str(response['main']['temp_min']) + ' °C',
                    'country_code': response['sys']['country'],
                    'wind': 'Wind: ' + str(response['wind']['speed']) + 'km/h',
                    'humidity': 'Humidity: ' + str(response['main']['humidity']) + '%',
                    'time': formatted_time
                }
                city_weather_updates.append(city_weather_update)

        context = {'city_weather_updates': city_weather_updates}
        return render(request, 'weatherupdates/home.html', context)
    except:
        return render(request, 'weatherupdates/404.html')

