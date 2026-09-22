import datetime
from fillpdf import fillpdfs
from pypdf import PdfReader, PdfWriter

# pdf_field_map = {
#     "patient_id": "row_Patient I.D Number",
#     "patient_hospital_number": "row_Patient Hospital Number",
#     "patient_surname": "row_Surname",
#     "patient_first_name": "row_First Name",
#     "patient_address": "patient_address",
#     "patient_tel": "row_Tel No.",
#     "patient_dob": "row_D.O.B.",
#     "patient_age": "row_Age",
#     "medical_aid": "row_Medical Aid",
#     "medical_aid_number": "row_Medical Aid Number",
#     "hospital": "row_Hospital/Clinic",
#     "ward": "row_Ward",
#     "diagnosis_reason": "diagnosis_reason",
#     "specimen": "row_Type of Specimen",
#     "date_taken": "row_Date Taken",
#     "time_taken": "row_Time",
#     "taken_by": "row_Taken By",
#     "doctor_name": "row_Requesting Health Care Worker",
#     "hpcsa_number": "row_HPCSA/SANC Number",
#     "doctor_contact": "row_Contact Numbers",
#     "doctor_email": "row_E-mail Address"
# }
pdf_field_map = {

    # Patient information
    "patient_name": "row_Surname",
    "date_of_birth": "row_D.O.B.",
    "patient_ID_number": "row_Patient I.D Number",
    "address": "patient_address",
    "sex": None,  # handled separately because PDF uses sex_m / sex_f

    # Clinical information
    "symptoms": "clinical_info",
    "diagnosis": "diagnosis_reason",

    # Tests
    "tests_requested": None,  # handled separately because these correspond to checkboxes

    # Requesting healthcare worker
    "requesting_healthcare_worker": "row_Requesting Health Care Worker",
    "HPCSA": "row_HPCSA/SANC Number",
    "contact_number": "row_Contact Numbers",
    "email_address": "row_E-mail Address",

    # Hospital information
    "hospital_name": "row_Hospital/Clinic",
    "ward_number": "row_Ward",
}

def populate(data):

    reader = PdfReader("Request_Form.pdf")
    writer = PdfWriter()

    writer.clone_document_from_reader(reader)

    pdf_data = {}

    for json_key, pdf_key in pdf_field_map.items():

        if pdf_key is None:
            continue

        if json_key in data:

            value = data[json_key]

            if value is not None and value != "":
                pdf_data[pdf_key] = str(value)

    reader = PdfReader("Request_Form.pdf")

    writer = PdfWriter()
    writer.clone_document_from_reader(reader)

    writer.update_page_form_field_values(
        writer.pages[0],
        pdf_data
    )

    with open("completed_form.pdf", "wb") as file:
        writer.write(file)

