import wave
import numpy as np
import matplotlib.pyplot as plt
import librosa

def visualizeSoundv1(filename, figsize = (16,5)):
    wav_obj = wave.open(f=filename, mode="rb")

    # Get wave properties
    sample_freq = wav_obj.getframerate()    # The sampling rate quantifies how many samples of the sound are taken every second
    n_samples = wav_obj.getnframes()
    signal_wave = wav_obj.readframes(n_samples)

    t_audio = n_samples/sample_freq
    signal_arr = np.frombuffer(signal_wave, dtype=np.int16)
    
    chanel = signal_arr[:]

    times = np.linspace(0, n_samples/sample_freq, num=n_samples)

    plt.figure(figsize=figsize)
    plt.plot(times, chanel)
    plt.title("Channel")
    plt.ylabel("Signal Value")
    plt.xlabel("Time (s)")
    plt.xlim(0, t_audio)
    plt.show()


def visualizeSoundv2(filename, figsize=(16,5)):
    signal, sample_rate = librosa.load(filename)
    print("hi")
    plt.figure(figsize=figsize)
    plt.plot(signal)
    plt.show()

visualizeSoundv2("D:\\VoiceClone\\Resource\\RONALDO SIU.wav")   
