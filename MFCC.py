import scipy.io.wavfile as wav
import numpy as np
import python_speech_features as psf
from sklearn.preprocessing import MinMaxScaler
from scipy.signal import resample

class MFCC:

    def __init__(self, file_path):

        self.sr,self.audio_data = wav.read(file_path)
        self.mfccs = None

    def calculate(self):
        factor = 16_000 / self.sr
        signal = resample(self.audio_data, int(self.audio_data.shape[0] * factor))
        self.mfccs = psf.mfcc(
            signal, 
            samplerate=self.sr, 
            nfft=1024,
            numcep=30
            )
        return self.mfccs

def mfcc_difference(mfcc1,mfcc2):
    scaler = MinMaxScaler()
    scaler.fit(mfcc1)

    mfcc1 = scaler.transform(mfcc1)
    mfcc2 = scaler.transform(mfcc2)

    return np.sqrt(np.sum((mfcc1 - mfcc2)**2))