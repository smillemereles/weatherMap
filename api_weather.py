import requests
import datetime as dt
from config import API_KEY

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

def handle_api_error(response):
    if response.status_code != 200:
        error_data = response.json()
        error_code = error_data.get("cod", "Unknown")
        error_message = error_data.get("message", "No error message provided")

        # Handling specific error codes
        error_messages = {
            400: f"Error {error_code}: Bad Request - {error_message}",
            401: f"Error {error_code}: Unauthorized - Check your API key.",
            429: f"Error {error_code}: Too Many Requests - Please try again later."
        }
        print(error_messages.get(error_code, f"Error {error_code}: {error_message}"))
        return False
    return True

def fetch_weather_data(city, unit):
    url = f"{BASE_URL}appid={API_KEY}&q={city}&units={unit}"
    try:
        response = requests.get(url)
        if not handle_api_error(response):
            return None
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to the weather service: {e}")
        return None

def process_weather_data(weather_data, city, unit):
    main_data = weather_data["main"]
    wind_data = weather_data["wind"]
    sys_data = weather_data["sys"]

    temp = main_data["temp"]
    feels_like = main_data["feels_like"]
    wind_speed = wind_data["speed"]
    humidity = main_data["humidity"]
    description = weather_data["weather"][0]["description"]
    sunrise_time = dt.datetime.fromtimestamp(sys_data["sunrise"], dt.timezone.utc)
    sunset_time = dt.datetime.fromtimestamp(sys_data["sunset"], dt.timezone.utc)

    temp_unit = "K" if unit == "standard" else ("C" if unit == "metric" else "F")

    return {
        "city": city,
        "temperature": f"{temp:.2f}",
        "feels_like": f"{feels_like:.2f}",
        "humidity": humidity,
        "wind_speed": wind_speed,
        "description": description,
        "sunrise": str(sunrise_time),
        "sunset": str(sunset_time),
        "temp_unit": temp_unit
    }