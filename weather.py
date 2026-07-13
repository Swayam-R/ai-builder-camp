import requests

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

country = input("Enter a country")
url = f"https://geocoding-api.open-meteo.com/v1/search?name={country}&count=1"
reply=requests.get(url)
dictionary1 = reply.json()
lat = dictionary1["results"][0]["latitude"]
lon = dictionary1["results"][0]["longitude"]
print (lat)
print(lon)
url2 = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"
reply2 = requests.get(url2)
dictionary2 = reply2.json()
current2 = dictionary2["current"]
print (current2)
temp2 = current2["temperature_2m"]
print("Temperature in "+country+" is "+temp2)
