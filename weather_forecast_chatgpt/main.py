from tkinter import Tk
from weather_forecast_chatgpt import WeatherApp

if __name__ == "__main__":
    # Create the main Tkinter application window
    root = Tk()

    # Instantiate the WeatherApp and run the Tkinter main loop
    app = WeatherApp(root)
    root.mainloop()
