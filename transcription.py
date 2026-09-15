import whisper

def transcribe(audio):
    #loading model 
    model = whisper.load_model("medium")

    #transcribe audio file
    result = model.transcribe(audio)

   #return transcription
    transcription = result["text"]
    return transcription