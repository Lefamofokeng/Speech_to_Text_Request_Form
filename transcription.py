import whisper

def transcribe(audio):
    #loading model 
    model = whisper.load_model("turbo")

    #transcribe audio file
    result = model.transcribe(
        audio,
        initial_prompt="""Expect South African names and surnames :
                        Lefa, Nkululeko, Mathebula, Mofokeng, Mokoena,Sipho, Sifiso, Themba, Mpho, Lerato, Thandiwe,
                        Nomalanga, Bongani, Zanele, Khumalo, Dlamini,
                        Nkosi, Mthembu, Ndlovu, Mokoena, Mahlangu, Themba. save emails in the example format: name@example.com"""
    )

    transcription = result["text"]
    return transcription