import datetime
from fillpdf import fillpdfs
from pypdf import PdfReader, PdfWriter

def populate():

    reader = PdfReader("Request_Form.pdf")
    writer = PdfWriter()

    writer.clone_document_from_reader(reader)

    data = {
        "row_Patient I.D Number": "9103125411077",
        "row_Surname": "Mokoena",
        "row_First Name": "Thato",
        "patient_address": "24 Kindred Ave, South Park",
        "row_Age": "42",
        'row_Date Taken': '24/02/2026', 
        'row_Time': '13h00', 
        'row_Taken By': 'Dr Jared Smith', 
        'row_Requesting Health Care Worker': 'Dr Jared Smith', 
        'row_HPCSA/SANC Number': 'HP1401636', 
        'row_Contact Numbers': '0112435467', 
        'row_E-mail Address': 'jared.smith@netcare.co.za'
    }

    writer.update_page_form_field_values(
        writer.pages[0],
        data
    )

    with open("completed_form.pdf", "wb") as f:
        writer.write(f)

populate()