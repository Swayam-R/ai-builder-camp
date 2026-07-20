import requests

import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("WEATHER_KEY")
print(key)

url = "https://api.open-meteo.com/v1/forecast?latitude=25.2&longitude=55.27&current=temperature_2m"

response = requests.get(url)

print(response.status_code)
print(response.text)
data = response.json()
print(data)
current = data["current"]
print(current)
temp = current["temperature_2m"]
print("Dubai ",temp)

country = input("Enter a country: ")
url = f"https://geocoding-api.open-meteo.com/v1/search?name={country}&count=1"
reply=requests.get(url)
dictionary1 = reply.json()
dictionary1 = reply.json()

if "results" not in dictionary1:
    print(f"Sorry, couldn't find a place called {country}.")
else:
    lat = dictionary1["results"][0]["latitude"]
    lon = dictionary1["results"][0]["longitude"]
    url2 = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
    reply2 = requests.get(url2)
    dictionary2 = reply2.json()
    if "current" not in dictionary2:
        print("Weather data unavailable for that location.")
    else:
        temp2 = dictionary2["current"]["temperature_2m"]
        print(f"Temperature in {country} is {temp2}°C")
