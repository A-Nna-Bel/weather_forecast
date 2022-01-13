"""
This code is used to get the weather forecast of 16 days
The requests librabry is imported to send request to the web through the  weather API key
The request is then printed in json format
"""

import requests

url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

city_name = input('Enter city name:')
querystring = {f"q":{city_name},"lat":"1","lon":"139","cnt":"10","units":"metric or imperial"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "c14a3d233bmshe860686baf25a54p171ec4jsn56fbc2ba662a"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.json())


