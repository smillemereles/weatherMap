#!/bin/bash

# Check if virtual environment exists, if not create one
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install or upgrade dependencies
pip install -r requirements.txt

# Function to run the weather app
run_weather_app() {
    echo "Running Weather App..."
    python main.py "$1" "$2" ${3:+--export "$3"}
}

# Check if correct number of arguments is provided
if [ "$#" -lt 2 ] || [ "$#" -gt 3 ]; then
    echo "Usage: $0 <city> <unit> [export_format]"
    echo "Example: $0 'New York' metric json"
    exit 1
fi

# Run the weather app with provided arguments
run_weather_app "$1" "$2" "$3"

# Deactivate virtual environment
deactivate

echo "Script execution completed."