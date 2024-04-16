import requests

fhir_server_base_url = "https://hapi.fhir.org/baseR4" 

# Get the CapabilityStatement
response = requests.get(f"{fhir_server_base_url}/metadata")
response.raise_for_status()  # Raise an error if the request fails

capability_statement = response.json()

# Extract supported resource types
supported_resources = capability_statement["rest"][0]["resource"]
supported_resource_types = [resource["type"] for resource in supported_resources]

# Print supported resources
print("Supported Resource Types:")
for resource_type in supported_resource_types:
    print(resource_type)
