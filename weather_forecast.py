import tkinter as tk
from tkinter import ttk
import requests

api_key = 'f02170a9e03fa8c9001e5acc6ef54cc7'

def get_weather_by_city(city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}  # You can change 'metric' to 'imperial' for Fahrenheit

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            result_text.set(
                            f"Temperature: {data['main']['temp']}°C\n\n"
                            f"Humidity: {data['main']['humidity']}%\n\n"
                            f"Wind Speed: {data['wind']['speed'] * 3.6: .2f} km/h\n\n"
                            f"Pressure: {data['main']['pressure']} hPa\n\n")

            # Check if precipitation data is available
            if 'rain' in data:
                precipitation_mm = data['rain']['1h']
                total_possible_precipitation = 10.0  # Replace with the total possible precipitation for the given period
                precipitation_percentage = (precipitation_mm / total_possible_precipitation) * 100

                result_text.set(result_text.get() +
                                f"Precipitation: {precipitation_percentage:.2f}% of possible precipitation\n")
            else:
                result_text.set(result_text.get() + "Precipitation: 0% (No precipitation)\n")

        else:
            result_text.set(f"Error: {data['message']}")

    except Exception as e:
        result_text.set(f"An error occurred: {e}")

def search_weather():
    city = city_entry.get()
    get_weather_by_city(city)

# Create the main application window
app = tk.Tk()
app.title("Weather Forecast")

font_style = ('Arial', 16)

# Create and place widgets in the window with added margins
label = ttk.Label(app, text="Location:", font=font_style)
label.grid(row=0, column=2, padx=(10, 5), pady=(10, 5))  # Added right and bottom margins

city_entry = ttk.Entry(app)
city_entry.grid(row=0, column=3, padx=(5, 5), pady=(10, 5))  # Added left and right margins

# Use the compound option to mimic a raised appearance
search_button = tk.Button(app, text="Search", command=search_weather, compound="center", relief="raised")
search_button.grid(row=0, column=4, padx=(5, 10), pady=(10, 5))  # Added left and bottom margins

result_text = tk.StringVar()
result_label = ttk.Label(app, textvariable=result_text, wraplength=400, font=font_style)
result_label.grid(row=1, column=0, columnspan=3, padx=(10, 10), pady=(5, 10))  # Added left and right margins

app.minsize(width=400, height=300)

# Run the application
app.mainloop()
