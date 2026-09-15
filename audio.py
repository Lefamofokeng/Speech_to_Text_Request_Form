import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

audio_bits = []


def audio_callback(samples_chunk, frames, time, status):

    #collection buffers for sound bits are stored here
    audio_bits.append(samples_chunk.copy()) 


def record_audio(filename="recording.wav", sampleRate=16000):

    print("Recording... press Enter to stop")
    audio_bits.clear()

    #setting up the connection to the microphone for recording
    stream = sd.InputStream(samplerate=sampleRate, channels=1, callback=audio_callback) 
    stream.start()

    # block execution until Enter is pressed
    input()  

    stream.stop()
    stream.close()

    audio = np.concatenate(audio_bits)
    wav.write(filename, sampleRate, audio)
    print("Recording saved")

    return filename