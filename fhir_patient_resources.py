import requests
import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt

def get_patient_ids():
    # Retrieve a list of patient IDs from the FHIR server
    url = 'http://hapi.fhir.org/baseR4/Patient?_count=25'
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        patient_ids = [entry['resource']['id'] for entry in data.get('entry', [])]
        return patient_ids
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving patient IDs: {e}")
        return []

def get_patient_data(resource_type, patient_id):
    url = f'http://hapi.fhir.org/baseR4/{resource_type}?subject=Patient/{patient_id}'
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving {resource_type} for patient {patient_id}: {e}")
        return None

def process_data(resource_type, data):
    attribute_count = 0
    if data and 'entry' in data:
        for entry in data['entry']:
            resource = entry['resource']
            attribute_count += len(resource.keys())
    return attribute_count

def main():
    patient_ids = get_patient_ids()
    all_data = []

    resource_types = [
        'Condition', 'AllergyIntolerance', 'MedicationRequest', 'Observation', 'Procedure',
        'DiagnosticReport', 'Immunization', 'CarePlan', 'Encounter', 'FamilyMemberHistory', 
        'CareTeam', 'Specimen', 'EpisodeOfCare'
    ]

    for patient_id in tqdm(patient_ids, desc="Processing patients"):
        patient_data = {'PatientID': patient_id}
        for resource_type in tqdm(resource_types, desc=f"Processing resources for patient {patient_id}", leave=False):
            data = get_patient_data(resource_type, patient_id)
            attribute_count = process_data(resource_type, data)
            patient_data[resource_type] = attribute_count
        all_data.append(patient_data)
    
    df = pd.DataFrame(all_data)
    df.to_excel("fhir_data_attributes.xlsx", index=False)


    resource_summary = df.sum().drop('PatientID')
    resource_summary.plot(kind='bar', figsize=(12, 6), title="Number of Attributes per FHIR Resource Type")
    plt.xlabel("Resource Type")
    plt.ylabel("Number of Attributes")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
