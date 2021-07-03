from django.shortcuts import render, redirect
import requests
from django.contrib import messages


# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=7b7375507ebfdc061b87633fd264fc74'
    if request.method == 'POST':
        city = request.POST['city']
        r = requests.get(url.format(city)).json()
        print(r)
        if r['cod'] == 200:

            weather_data = {
                'country': r['sys']['country'],
                'city': city,
                'temperature': r['main']['temp'],
                'humidity': r['main']['humidity'],
                'max_temp' : r['main']['temp_max'],
                'min_temp': r['main']['temp_min'],
                'description': r['weather'][0]['description'],
                'icon': r['weather'][0]['icon'],
            }
            context = {'weather_data': weather_data}
            return render(request, 'home.html', context)
        else:
            messages.info(request, 'City not found')
            return redirect('/')
    else:
        return render(request,'home.html')


