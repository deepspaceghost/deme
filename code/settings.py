from datetime import datetime
from geopy.geocoders import Nominatim
from requests import get

ATS = 0.833 # average typing speed

# getting and formetted the current time
ct = datetime.now().time()
current_formatted_time = ct.strftime("%H:%M")

# getting the location
geolocator = Nominatim(user_agent="geoapiExercises")
latitude = "LATITUDE"
longitude = "LONGITUDE"
location = geolocator.reverse(latitude + "," + longitude)
address = location.raw["address"]
city = address.get("city", "")

# uses the time and location to get the weather data
WEATHER_TOKEN = "TOKEN"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "CITY"
complete_url = base_url + "&appid=" + WEATHER_TOKEN + "&q=" + city_name + "&units=imperial"
response = get(complete_url)
weather_list = response.json()
y = weather_list["main"]
current_temperature = round(y["temp"])
z = weather_list["weather"]
weather_description = z[0]["description"]

# Lists of strings Persephone will listen out for

archer_phrasing_phrases = [
    "begging for it",
    "gaping hole",
    "just the tip",
    "my box"
]

better_adjectives = [
    "better", "good", "well"
]

byte_nouns = [
    "byte", "bytes"
]

convert_verbs = [
    "convert", "converted"
]

define_verbs = [
    "define", "defined", "defines", "defining"
]

do_verbs = [
    "do", "done"
]

eat_verbs = [
    "ate", "eat", "eaten", "eating", "eats"
]

how_are_you_phrases = [
    "how are you, Deme?",
    "how r you, Deme",
    "how are u, Deme?",
    "how r u, Deme?",
    "how're you, Deme?",
    "how're u, Deme?"
]

message_nouns = [
    "message", "messages"
]

object_nouns = [
    "object", "objects"
]

possible_actions = [
    "paper",
    "rock",
    "scissors"
]

thank_you_variants = [
    "thank u",
    "thank you",
    "thanks",
    "thanx",
    "thnx"
]

tooth_nouns = [
    "teeth", "tooth"
]

try_verbs = [
    "tried", "tries", "try", "trying"
]

yourself_pronouns = [
    "yourself", "yourselves"
]
