from audio import record_audio
from transcription import transcribe
from llm import medical_data_extraction
from llm import json_exporter
#audio_file = record_audio()
transcript = transcribe("recording.wav")
data_fields = medical_data_extraction(transcript)
json = json_exporter(data_fields)
print(transcript)
print("")
# print(data_fields)
print(json)