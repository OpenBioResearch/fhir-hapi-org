"""
This script interacts with a FHIR server to fetch available resource types and save them to a CSV file.
"""

import csv
import requests

# Define the base URL of the FHIR server
fhir_server_url = "https://hapi.fhir.org/baseR4/metadata"


# Function to fetch resource types from the FHIR server
def fetch_resource_types_and_info(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        resource_types = []
        for resource in data.get("rest", [])[0].get("resource", []):
            resource_types.append(resource.get("type"))
        return resource_types
    except requests.RequestException as e:
        print(f"Error fetching resource types: {e}")
        return []


# Function to save resource types to a CSV file
def save_to_csv(resource_types, filename="fhir_resource_types.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Resource Type"])
        for resource_type in resource_types:
            writer.writerow([resource_type])


# Main function to fetch resource types and save them to a CSV
def main():
    print("Fetching resource types from FHIR server...")
    resource_types = fetch_resource_types_and_info(fhir_server_url)
    if resource_types:
        print(f"Successfully fetched {len(resource_types)} resource types.")
        save_to_csv(resource_types)
        print("Successfully saved resource types to CSV.")
    else:
        print("Failed to fetch resource types.")


if __name__ == "__main__":
    main()
