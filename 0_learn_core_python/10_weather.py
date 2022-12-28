import requests

api_key = "<api_key>"
lat = "<latitude>"
lon = "<longitude>"
exclude = "hourly,daily" #part, hourly,daily
units = "imperial"
#url - https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&exclude={part}&appid={API key}
url = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&exclude=" + exclude + "&appid=" + api_key  + "&units=" + units

request = requests.get(url)
print(request)
#output - <Response [200]>

json = request.json();
#print(json)
#output - {'coord': {'lon': -1.5158, 'lat': 55.0338}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 'base': 'stations', 'main': {'temp': 45.1, 'feels_like': 41.34, 'temp_min': 42.39, 'temp_max': 46.49, 'pressure': 1000, 'humidity': 84}, 'visibility': 10000, 'wind': {'speed': 6.91, 'deg': 260}, 'clouds': {'all': 40}, 'dt': 1672182238, 'sys': {'type': 2, 'id': 2004181, 'country': 'GB', 'sunrise': 1672129880, 'sunset': 1672155752}, 'timezone': 0, 'id': 3236250, 'name': 'Shiremoor', 'cod': 200}

description = json.get("weather")[0].get("description")
print("Today's forcast is", description)

temp_min = json.get("main").get("temp_min")
print("The minimum temperature is", temp_min)

temp_max = json.get("main").get("temp_max")
print("The maxmum temperature is", temp_max)






