def show_help():
    print("Weather App Usage:")
    print("1. Enter a city name when prompted.")
    print("2. Choose a unit system (standard, metric, or imperial).")
    print("3. Optionally select an export format (csv, json, or txt).")
    print("4. View the weather information in the console.")
    print("5. If an export format was chosen, find the exported file in the same directory.")

def display_weather_info(weather_info):
    print(f"\nWeather in {weather_info['city']}:")
    print(f"Temperature: {weather_info['temperature']}°{weather_info['temp_unit']}")
    print(f"Feels like: {weather_info['feels_like']}°{weather_info['temp_unit']}")
    print(f"Humidity: {weather_info['humidity']}%")
    print(f"Wind speed: {weather_info['wind_speed']} m/s")
    print(f"Description: {weather_info['description']}")
    print(f"Sunrise: {weather_info['sunrise']} UTC")
    print(f"Sunset: {weather_info['sunset']} UTC")