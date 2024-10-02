import csv
import json

def export_data(data, filename, file_format):
    try:
        if file_format == "csv":
            with open(filename, "w", newline="") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=data.keys())
                writer.writeheader()
                writer.writerow(data)
        elif file_format == "json":
            with open(filename, "w") as jsonfile:
                json.dump(data, jsonfile, indent=4)
        elif file_format == "txt":
            with open(filename, "w") as txtfile:
                for key, value in data.items():
                    txtfile.write(f"{key}: {value}\n")
        print(f"Weather data has been exported to {filename}")
    except IOError as e:
        print(f"Error exporting data: {e}")