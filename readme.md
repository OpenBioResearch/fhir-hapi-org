# fhir-hapi-server

## Project Overview

The primary purpose of the FHIR HAPI Test Server http://hapi.fhir.org is to provide a platform for testing, developing, and experimenting with FHIR (Fast Healthcare Interoperability Resources) APIs and resources. It is designed to simulate a real FHIR server.

These simple python scripts enable interacting with FHIR resources at http://hapi.fhir.org/baseR4, retrieving anonymized patient IDs, providing available resource types for testing and visualizing the number of attributes (ie medications) associatd with each FHIR resource type.  


## Usage


**Clone the repository:**

```bash
git clone https://github.com/OpenBioResearch/fhir-hapi-org.git
cd fhir-hap-org
```

**Create a virtual environment (optional but recommended):**

```bash 
python -m venv .venv
source .venv/bin/activate  # git bash
```
**Install the Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Python Scripts

To run the Python scripts, use the following commands:

```bash
python fhir_resource_types.py
python fhir_patient_resources.py
python idc_nonduplicates_metadata.py

**Outputs**
    fhir_resource_types.csv (list of test fhir resources available)
    fhir_data_attributes.xlsx (spreadsheet of attributes and record counts)

## License
This project is licensed under the Apache License 2.0 (LICENSE). 
https://hapifhir.io/hapi-fhir/license.html

