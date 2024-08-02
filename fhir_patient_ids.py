"""
This module provides a function to retrieve patient resource IDs from a FHIR server.
"""

import requests


def get_patient_resource_ids(fhir_server_url="http://hapi.fhir.org/baseR4", timeout=10):
    """
    Returns:
        list: A list of patient resource IDs (strings) or an empty list if none are found.
    """
    patient_resource_ids = []
    url = f"{fhir_server_url}/Patient"
    headers = {"Accept": "application/fhir+json"}

    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()

        # Check if there are entries in the response
        if "entry" in data:
            for entry in data["entry"]:
                patient_resource_ids.append(entry["resource"]["id"])
        else:
            print(
                "No patient resources found."
            )  # Inform when no patient resources are found

    except requests.exceptions.RequestException as e:
        print(f"Error retrieving patient IDs: {e}")

    return patient_resource_ids


if __name__ == "__main__":
    patient_ids = get_patient_resource_ids()
    if patient_ids:
        print("Retrieved patient resource IDs:")
        for patient_id in patient_ids:
            print(patient_id)
    else:
        print(
            "No patient resources found."
        )  
