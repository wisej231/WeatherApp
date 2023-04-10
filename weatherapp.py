'''
Weather App Created by Jackson Wise 4/7/2023
'''

import requests
import tkinter as tk


root = tk.Tk()
root.geometry("375x300")
root.title("Weather App")

def get_city_data():
    cityInput = inputtxt.get(1.0, "end-1c")
    access_key = inputaccess.get(1.0, "end-1c")
    url = "http://api.weatherstack.com/current"
    credentials = { "access_key": access_key, "query": cityInput }
    response = requests.get(url, params=credentials)

    if response.status_code == 200:
        data = response.json()

        #Location Data
        location = data["location"]["name"]
        current_time = data["location"]["localtime"]

        #Current Weather Data
        temperature_C = data["current"]["temperature"]
        temperature_F = (temperature_C*(9/5))+32
        feels_like_C = data["current"]["feelslike"]
        feels_like_F = (feels_like_C*(9/5))+32
        description = data["current"]["weather_descriptions"][0]
        wind_speed = data["current"]["wind_speed"]
        precipitation = data["current"]["precip"]

        location_string=f"\nCurrent Weather in {location} at {current_time}: is {description}, "
        temperature_string=f"\nTemperature is: {temperature_F} \u00B0F, but it feels like {feels_like_F} \u00B0F"
        misc_string=f"\nThe Wind Speed is: {wind_speed} km/h, and the Precipitation level is {precipitation}"

        out=location_string+temperature_string+misc_string
    else:
        out="Error: The city you have entered is not in our database"

    label.config(text = out)


#Textbox Creation
inputtxt = tk.Text(root, height=2, width=20)
inputtxt.pack()

#Button Creation
button = tk.Button(root, text="Enter a city to get the weather", command=get_city_data)
button.pack()

#Api Access Key
accesslabel = tk.Label(root, text="Enter your WeatherStack API access key below")
accesslabel.pack()

inputaccess = tk.Text(root, height= 2, width = 20)
inputaccess.pack()

#Label Creation
label = tk.Label(root, text="")
label.pack()

root.mainloop()
