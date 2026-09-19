import ollama

output_format = {
    "type": "object",
    "properties": {
        "patient_name": {"type": ["string", "null"]},
        "date_of_birth": {"type": ["string", "null"]},
        "patient_ID_number": {"type": ["string", "null"]},
        "address": {"type": ["string", "null"]},
        "sex": {"type": ["string","null"]},
        "symptoms": {"type":["string","null"]},
        "diagnosis": {"type": ["string", "null"]},
        "tests_requested": {
            "type": ["array", "null"],
            "items": {"type": "string"}
        },
        "requesting_healthcare_worker":{"type": ["string", "null"]},
                "HPCSA":{"type": ["string", "null"]},
                "contact_number":{"type": ["string", "null"]},
                "email_address":{"type": ["string", "null"]},
                "hospital_name": {"type":["string","null"]},
                "ward_number": {"type":["string","null"]}
    },
    "required": [
        "patient_name",
        "date_of_birth",
        "patient_ID_number",
        "address",
        "sex",
        "symptoms",
        "diagnosis",
        "tests_requested",
        "requesting_healthcare_worker",
        "HPCSA",
        "contact_number",
        "email_address",
        "hospital_name",
        "ward_number"
    ]
}

def medical_data_extraction(transcript):
    response = ollama.chat(
        model="llama3.1:8b",
        format= output_format,
        messages=[
            {
                "role": "system",
                "content": """Extract the following information from the transcript:
                
                Patient:
                patient_name
                date_of_birth
                patient_ID_number
                address
                sex
                symptoms
                diagnosis
                tests_requested (return as a list of tests)
                
                Healthcare Worker:
                requesting_healthcare_worker
                HPCSA
                contact_number
                email_address (return as email address format: namesurname@example.com. No punctuation unlesss explicitly stated )
                hospital_name
                ward_number

                Do not invent information.
                If information is not provided return null."""
            },
            {
                "role": "user",
                "content": transcript
            }
        ]
    )

    output = response["message"]["content"]
    return output