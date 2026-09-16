import whisper

def transcribe(audio):
    #loading model 
    model = whisper.load_model("turbo")

    #transcribe audio file
    result = model.transcribe(
        audio,
        initial_prompt="""This conversation contains South African names such as:
                        Lefa, Nkululeko, Mathebula, Mofokeng, Mokoena,Sipho, Sifiso, Themba, Mpho, Lerato, Thandiwe,
                        Nomalanga, Bongani, Zanele, Khumalo, Dlamini,
                        Nkosi, Mthembu, Ndlovu, Mokoena, Mahlangu, Themba."""
    )

    transcription = result["text"]
    return transcription