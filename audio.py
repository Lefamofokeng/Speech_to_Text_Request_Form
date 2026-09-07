import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import threading

import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav

audio_bits = []


def audio_callback(indata, frames, time, status):
    audio_bits.append(indata.copy())


def record_audio(filename="recording.wav", sampleRate=16000):
    print("Recording... press Enter to stop")
    audio_bits.clear()

    stream = sd.InputStream(samplerate=sampleRate, channels=1, callback=audio_callback)
    stream.start()
    input()  # blocks until you press Enter
    stream.stop()
    stream.close()

    audio = np.concatenate(audio_bits)
    wav.write(filename, sampleRate, audio)
    print("Recording saved")

    return filename