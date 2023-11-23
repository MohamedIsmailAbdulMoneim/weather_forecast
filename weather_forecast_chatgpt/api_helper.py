import requests

API_KEY = 'f02170a9e03fa8c9001e5acc6ef54cc7'

def get_weather_by_city(city):
    """
    Get weather information for a given city using the OpenWeatherMap API.

    Args:
        city: The name of the city for which weather information is requested.

    Returns:
        A dictionary with 'success' indicating the success of the operation and 'message' containing the result or error.
    """
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed_m_s = data['wind']['speed']
            pressure = data['main']['pressure']

            # Display wind speed in km/h
            wind_speed_km_h = wind_speed_m_s * 3.6

            result = (
                      f"Temperature: {temperature}°C\n\n"
                      f"Humidity: {humidity}%\n\n"
                      f"Wind Speed: {wind_speed_km_h:.2f} km/h\n\n"
                      f"Pressure: {pressure} hPa\n\n")

            # Check if precipitation data is available
            if 'rain' in data:
                precipitation_mm = data['rain']['1h']
                total_possible_precipitation = 10.0
                precipitation_percentage = (precipitation_mm / total_possible_precipitation) * 100

                result += (f"Precipitation: {precipitation_percentage:.2f}% of possible precipitation\n")
            else:
                result += "Precipitation: 0% (No precipitation)\n"

            return {'success': True, 'message': result}

        else:
            return {'success': False, 'message': f"Error: {data['message']}"}

    except requests.exceptions.RequestException as e:
        return {'success': False, 'message': f"Error: {e}"}
