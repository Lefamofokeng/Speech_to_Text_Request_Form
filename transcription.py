import whisper

def transcribe(audio):
    # Load the model (downloads it the first time)
    model = whisper.load_model("base")

    # Transcribe an audio file
    result = model.transcribe(audio)

    # Print the recognized speech
    #print(result["text"])

   # return transcription
    transcription = result["text"]
    return transcription