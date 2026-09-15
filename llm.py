import ollama

"""
Patient John Smith, born 12 March 1985.
He has suspected tuberculosis.
Please perform a sputum test."""

def medical_data_extraction(transcript):
    response = ollama.chat(
        model="llama3.1:8b",
        messages=[
            {
                "role": "system",
                "content": """Extract the following information from the transcript:

                patient_name
                date_of_birth
                patient_number
                diagnosis
                tests_requested (return as a list of tests)

                If information is not provided return null
                Do not invent information
                Return ONLY JSON."""
            },
            {
                "role": "user",
                "content": transcript
            }
        ]
    )

    output = response["message"]["content"]
    return output



