import wave
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

class MFCC:
    def load_audio(file_path):
        with wave.open(file_path, "rb") as wav:
            audio_data = wav.readframes(wav.getnframes())
            sample_rate = wav.getframerate()

            audio_data = np.frombuffer(audio_data, dtype=np.int16)
        return audio_data, sample_rate

    def __init__(self, file_path):
        self.audio_data,self.sr = self.load_audio(file_path)
        self.mfccs = None

    def calculate(self):
        _,_, mfccs = plt.specgram(self.audio_data, Fs=self.sr)
        
        return 

def mfcc_difference(mfcc1,mfcc2):
    scaler = MinMaxScaler()
    scaler.fit(mfcc1)

    mfcc1 = scaler.transform(mfcc1)
    mfcc2 = scaler.transform(mfcc2)

    return np.sqrt(np.sum((mfcc1 - mfcc2)**2))