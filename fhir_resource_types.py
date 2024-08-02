"""
This script connects to a test FHIR server, retrieves resource types and saves them to a CSV file named 'fhir_resource_types.csv.
"""

import csv
import requests

# FHIR server
fhir_server_url = "https://hapi.fhir.org/baseR4/metadata"

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


def save_to_csv(resource_types, filename="fhir_resource_types.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Resource Type"])
        for resource_type in resource_types:
            writer.writerow([resource_type])


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
