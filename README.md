# FORECASTWEATHER
# Weather App

A command-line interface (CLI) application for fetching and displaying weather information using the OpenWeatherMap API.

## Features

- Fetch current weather data for any city
- Support for multiple temperature units (standard, metric, imperial)
- Error handling for API requests
- Data export functionality (CSV, JSON, TXT)
- User-friendly command-line interface

## Files

- `main.py`: Entry point of the application, handles CLI arguments
- `api_weather.py`: Manages API interactions and data processing
- `data_export.py`: Handles exporting weather data to various formats
- `user_interface.py`: Contains functions for displaying information to the user

## Usage

```
python main.py <city> <unit> [--export {csv,json,txt}]
```

- `<city>`: Name of the city to get weather information for
- `<unit>`: Temperature unit system (standard, metric, or imperial)
- `--export`: Optional argument to export data in CSV, JSON, or TXT format

## Example

```
python main.py London metric --export json
```

This command will fetch weather data for London in metric units and export it to a JSON file.

## Requirements

- Python 3.x
- `requests` library

## Setup

1. Clone the repository
2. Install required dependencies: `pip install requests`
3. Add your OpenWeatherMap API key to `config.py`

## Note

Make sure to keep your API key confidential and not share it publicly.