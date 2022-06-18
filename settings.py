from datetime import datetime
# from os import environ
# from geopy.geocoders import Nominatim
# from requests import get

ATS = 0.833 # average typing speed
# token = environ['TOKEN'] Discord token

# getting and formatting the current time
ct = datetime.now().time()
current_formatted_time = ct.strftime("%H:%M")

# getting the location
# geolocator = Nominatim(user_agent="geoapiExercises")
# latitude = "LATITUDE"
# longitude = "LONGITUDE"
# location = geolocator.reverse(latitude + "," + longitude)
# address = location.raw["address"]
# city = address.get("city", "")

# uses the time and location to get the weather data
# WEATHER_TOKEN = "TOKEN"
# base_url = "http://api.openweathermap.org/data/2.5/weather?"
# city_name = "CITY"
# complete_url = base_url + "&appid=" + WEATHER_TOKEN + "&q=" + city_name + "&units=imperial"
# response = get(complete_url)
# weather_list = response.json()
# y = weather_list["main"]
# current_temperature = round(y["temp"])
# z = weather_list["weather"]
# weather_description = z[0]["description"]
