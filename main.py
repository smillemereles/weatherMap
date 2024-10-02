import argparse
from api_weather import fetch_weather_data, process_weather_data
from data_export import export_data
from user_interface import show_help, display_weather_info

def main():
    # Configure argument parser
    parser = argparse.ArgumentParser(description='Weather Application CLI')
    parser.add_argument('city', type=str, help='City name to get the weather for')
    parser.add_argument('unit', choices=['standard', 'metric', 'imperial'], help='Unit system to use')
    parser.add_argument('--export', choices=['csv', 'json', 'txt'], help='Optional export format for the weather data')

    args = parser.parse_args()

    # Show help if necessary
    if args.city == '-help' or args.city == '/help':
        show_help()
        return

    # Get weather data
    weather_data = fetch_weather_data(args.city, args.unit)
    if weather_data:
        # Process weather data
        weather_info = process_weather_data(weather_data, args.city, args.unit)

        # Export data if a valid format is provided
        if args.export:
            filename = f"weather_data_{args.city}.{args.export}"
            export_data(weather_info, filename, args.export)

        # Display weather information
        display_weather_info(weather_info)

if __name__ == "__main__":
    main()