# fhir-hapi-server

## Project Overview

The `fhir-hapi` project is a resource for developers to test and develop using a demo Fast Healthcare Interoperability Resources (FHIR) tool which leverges the HAPI FHIR library. 

My simple python scripts enables interacting with  FHIR resources at http://hapi.fhir.org/baseR4, retrieving anonymized patient IDs, providing available resource types for testing and visualizing the number of attributes associatd with each FHIR resource type.  


## Usage

**Install the Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

**Run the python scriptS:**
    fhir_resource_types.py
    python fhir_patient_resources.py
    fhir_patient_ids.py

**Outputs**
    fhir_resource_types.csv (list of test fhir resources available)
    fhir_data_attributes.xlsx (spreadsheet of attributes and record counts)

## License
This project is licensed under the Apache License 2.0 (LICENSE). 
https://hapifhir.io/hapi-fhir/license.html

