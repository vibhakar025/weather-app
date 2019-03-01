from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
from django.http import HttpResponseRedirect

def index(request):
    url ='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=bebc7b09fdc7670a2138def452463f90'
    
    
    if request.method=='POST':
        form = CityForm(request.POST)
        form.save()

    cities=City.objects.all()
    
    weather_data=[]

    form=CityForm()

    for city in cities:
        r = requests.get(url.format(city)).json()
        i=1
        city_weather={
            'id': i,
            'city':city.name,
            'temperature':r["main"]["temp"],
            'description':r["weather"][0]["description"],
            'icon':r["weather"][0]["icon"],
        }
        i+=1
        weather_data.append(city_weather)

    print(weather_data)
    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/weather.html', context)


def delete(request, cityn):
    ci=City.objects.get(id=cityn)
    ci.delete()
    return render(request, 'weather/weather.html')