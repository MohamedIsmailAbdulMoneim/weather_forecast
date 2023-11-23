import tkinter as tk
from tkinter import ttk
from api_helper import get_weather_by_city

class WeatherApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Weather Forecast")
        self.master.geometry("600x400")
        self.master.minsize(width=400, height=300)

        self.font_style = ('Arial', 16)

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.master, text="Location:", font=self.font_style).grid(row=0, column=2, padx=(10, 5), pady=(10, 5))

        self.city_var = tk.StringVar()
        city_entry = ttk.Entry(self.master, textvariable=self.city_var)
        city_entry.grid(row=0, column=3, padx=(5, 5), pady=(10, 5))

        ttk.Button(self.master, text="Search", command=self.search_weather).grid(row=0, column=4, padx=(5, 10), pady=(10, 5))

        self.result_text = tk.StringVar()
        ttk.Label(self.master, textvariable=self.result_text, wraplength=400, font=self.font_style).grid(
            row=1, column=0, columnspan=3, padx=(10, 10), pady=(5, 10))

    def search_weather(self):
        city = self.city_var.get()
        result = get_weather_by_city(city)

        if result['success']:
            self.result_text.set(result['message'])
        else:
            self.result_text.set(f"Error: {result['message']}")
