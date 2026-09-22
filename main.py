from audio import record_audio
from transcription import transcribe
from llm import medical_data_extraction
from toJson import json_exporter
from validator import validate
from pdf_filler import populate
#audio_file = record_audio()
transcript = transcribe("clinician_recording3.mp3")
data_fields = medical_data_extraction(transcript)
json = json_exporter(data_fields)
valid_data = validate(json)
print("")
print("")
print(transcript)
print("")
# print(data_fields)
print("")
# print(json)
# print("")
#print(validate(json))
populate(valid_data)