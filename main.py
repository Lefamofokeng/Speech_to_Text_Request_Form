from audio import record_audio
from transcription import transcribe

audio_file = record_audio()
transcript = transcribe(audio_file)
print(transcript)