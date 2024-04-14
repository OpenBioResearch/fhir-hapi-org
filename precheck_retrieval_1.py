import requests

def get_patient_resource_ids(fhir_server_url="http://hapi.fhir.org/baseR4", timeout=10):
    """
    Retrieves patient resource IDs from the HAPI FHIR test server with a timeout.

    Args:
        fhir_server_url (str, optional): The URL of the FHIR server. Defaults to "http://hapi.fhir.org/baseR4".
        timeout (int, optional): The timeout in seconds for the request. Defaults to 10.

    Returns:
        list: A list of patient resource IDs (strings) if successful, or an empty list if no patients are found.
    """

    url = f"{fhir_server_url}/Patient"  # Construct the URL for Patient resources
    headers = {"Accept": "application/fhir+json"}  # Specify JSON format

    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()  # Raise an exception for non-2xx status codes

        data = response.json()
        patient_resource_ids = []  # Declare patient_resource_ids inside the try block

        if data.get("entry"):
            for entry in data["entry"]:
                resource_id = entry["resource"]["id"]  # Declare resource_id inside the loop
                patient_resource_ids.append(resource_id)

        return patient_resource_ids

    except requests.exceptions.RequestException as e:
        print(f"Error retrieving patient IDs: {e}")

    return []  # Return an empty list on errors


if __name__ == "__main__":
    patient_resource_ids = get_patient_resource_ids()
    if patient_resource_ids:
        print("Retrieved patient resource IDs:")
        for resource_id in patient_resource_ids:
            print(resource_id)
    else:
        print("No patient resources found.")
