from scipy.io import wavfile
import noisereduce as nr
import librosa
# load data
path = "D:\\VoiceDataTraining\\CN-Hutao\\vo_hutao_draw_appear.wav"
rate, data = wavfile.read(path)

# perform noise reduction
reduced_noise = nr.reduce_noise(y=data, sr=rate)
wavfile.write("mywav_reduced_noise.wav", rate, reduced_noise)