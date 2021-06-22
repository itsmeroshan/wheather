import requests
from datetime import datetime

api_key = '079cb7a7ee247bec53b7f00ceac6eb51'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
with open("main.py.txt","w") as report:

    report.write ("\n-------------------------------------------------------------")
    report.write("\nWeather Stats for - {}  || {}".format(location.upper(), date_time))
    report.write("\n-------------------------------------------------------------")

    report.write("\nCurrent temperature is: {:.2f} deg C".format(temp_city))
    report.write("\nCurrent weather desc  :" + weather_desc)
    report.write("\nCurrent Humidity      :" + str(hmdt) +'%')
    report.write("\nCurrent wind speed    :" + str(wind_spd) + 'kmph')