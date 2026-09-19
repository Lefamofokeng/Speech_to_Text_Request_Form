from toJson import json_exporter

def validate(json_output):
    FIELDS_TO_VERIFY = ["patient_name",
                        "patient_ID_number",
                        "requesting_healthcare_worker",
                        "contact_number",
                        "email_address",
                        "hospital_name"
                        ]
    for field in FIELDS_TO_VERIFY:
        if field not in json_output:
                continue
        print("Please verify these fields:")
        print(f"{field}: {json_output[field]}")

        choice = input("Is this correct? (y/n): ")
        if(choice.lower() == "n"):
             new_value = input("Enter correct value: ")
             json_output[field] = new_value

    print(json_output)

