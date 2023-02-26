import requests

def kelvinToCelsius(kelvin):
    return kelvin - 273.15

#API_KEY =  YOUR API KEY
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

cities = []
weathers = []
temperatures = []

amount = int(input("Enter the number of cities where you want to check the weather: "))
for i in range(0,amount):
    cities.append(input("Enter a city name: "))

print("##################################")

for city in cities:
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        weathers.append(data['weather'][0]['description'])
        temperatures.append(data['main']['temp'])
    else:
        print("An error occurred.")

for i in range(0, amount):
    print("City: " + cities[i])
    print("Weather: " + weathers[i])
    print("Temperature: " + str(round(kelvinToCelsius(temperatures[i]),2)) + "\xb0")
    print("##################################")
