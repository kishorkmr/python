import requests

def get_weather_desc_and_temp():
    api_key = "<api_key>"
    lat = "<latitude>"
    lon = "<longitude>"
    exclude = "hourly,daily" #part, hourly,daily
    units = "imperial"
    url = "https://api.openweathermap.org/data/2.5/weather?lat=" + lat + "&lon=" + lon + "&exclude=" + exclude + "&appid=" + api_key  + "&units=" + units

    request = requests.get(url)
    json = request.json();
    
    description = json.get("weather")[0].get("description")
    temp_min = json.get("main").get("temp_min")
    temp_max = json.get("main").get("temp_max")

    return {"description":description,
            "temp_min":temp_min,
            "temp_max":temp_max
            }

def main():
    weather_dict = get_weather_desc_and_temp()
    print("Today's forcast is", weather_dict.get("description"))
    print("The minimum temperature is", weather_dict.get("temp_min"))
    print("The maxmum temperature is", weather_dict.get("temp_max"))

main()




