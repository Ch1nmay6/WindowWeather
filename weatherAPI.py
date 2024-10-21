import tkinter as tk
import requests

window = tk.Tk()
window.title("Weather Dashboard")

labelCity = tk.Label(window, text='Enter City name: ')
labelCity.pack(pady=5)

entryCity = tk.Entry(window)
entryCity.pack(pady=5)


def weather():
    city = entryCity.get().strip()
    apiKey = '60f80ff8098c33b5d3909ca9092b1572'
    baseUrl = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric"

    response  = requests.get(baseUrl)
    
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather = data['weather'][0]

        result_text = (f"City: {city}\n"
                       f"Temperature: {main['temp']}°C\n"
                       f"Humidity: {main['humidity']}%\n"
                       f"Weather: {weather['description']}\n"
                       f"Wind Speed: {wind['speed']} m/s")
        
        # Update the result label with weather info
        resultLabel.config(text=result_text)
    else:
        resultLabel.config(text="Error: City not found or API request failed.")

buttonGetWeather = tk.Button(window, text='Get Weather', command=weather)
buttonGetWeather.pack(pady=10)

resultLabel = tk.Label(window, text='', justify=tk.LEFT)
resultLabel.pack(pady=5)

window.mainloop()