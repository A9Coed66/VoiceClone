import pyaudio
import wave 
# import audioDenose
# from audioDenoise import denoise
from audioDenoise.denoise import AudioDeNoise 

audio = pyaudio.PyAudio()

stream = audio.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

frames = []

try:
    while True:
        data = stream.read(1024)
        frames.append(data)
except KeyboardInterrupt:
    pass

stream.stop_stream()
stream.close()
audio.terminate()

sound_file = wave.open("myrecording.wav", "wb")
sound_file.setnchannels(1)
sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
sound_file.setframerate(44100)
sound_file.writeframes(b''.join(frames))
sound_file.close()

audioDenoiser = AudioDeNoise(inputFile="myrecording.wav")
audioDenoiser.deNoise(outputFile="myrecording_denoised.wav")
audioDenoiser.generateNoiseProfile(noiseFile="myrecording_noise_profile.wav")