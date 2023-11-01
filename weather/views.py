from django.shortcuts import render
import requests as re

# Create your views here.

def weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = 'daf7f070e9f003b5b6b90e25bfabc4c5'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        response = re.get(url)
        data = response.json()
        if data['cod'] == 200:  # Check if the response code is 200 (OK)
            context = {'data': data}
            return render(request, 'weather/weather.html', context)
        else:
            error_message = 'Invalid city. Please enter a valid city name.'
            context = {'error_message': error_message}
            return render(request, 'weather/weather.html', context)
    return render(request, 'weather/weather.html')
