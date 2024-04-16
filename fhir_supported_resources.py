import requests
import csv
import time

fhir_server_base_url = "https://hapi.fhir.org/baseR4"

def get_resource_description(resource_type):
    """Fetches a brief description of the resource type."""
    response = requests.get(f"{fhir_server_base_url}/{resource_type}")
    if response.status_code == 200:
        return response.json().get('text', {}).get('div')  
    else:
        return "Description not found"

# Get the CapabilityStatement
response = requests.get(f"{fhir_server_base_url}/metadata")
response.raise_for_status()  # Raise an error if the request fails

capability_statement = response.json()

# Extract supported resource types
supported_resources = capability_statement["rest"][0]["resource"]
supported_resource_types = [resource["type"] for resource in supported_resources]

# Export to CSV with descriptions
with open('supported_resources.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Resource Type', 'Description'])  # Write the header row

    for i, resource_type in enumerate(supported_resource_types):
        description = get_resource_description(resource_type)
        writer.writerow([resource_type, description])
        print(f"Progress: {i+1}/{len(supported_resource_types)} resources processed") 
        time.sleep(0.1)  # Small delay to make progress readable

