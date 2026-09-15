import ollama

output_format = {
    "type": "object",
    "properties": {
        "patient_name": {"type": ["string", "null"]},
        "date_of_birth": {"type": ["string", "null"]},
        "patient_number": {"type": ["string", "null"]},
        "diagnosis": {"type": ["string", "null"]},
        "tests_requested": {
            "type": ["array", "null"],
            "items": {"type": "string"}
        }
    },
    "required": [
        "patient_name",
        "date_of_birth",
        "patient_number",
        "diagnosis",
        "tests_requested"
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
                
                patient_name
                date_of_birth
                patient_number
                diagnosis
                tests_requested (return as a list of tests)

                Do not invent information."""
            },
            {
                "role": "user",
                "content": transcript
            }
        ]
    )

    output = response["message"]["content"]
    return output



