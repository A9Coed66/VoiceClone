import numpy as np
import librosa
import soundfile

def removeSilent(y, sr, top_db = 10):
    intervals = librosa.effects.split(y, top_db)
    tmp = y[intervals[0][0]:intervals[0]:[1]]
    for i in range(1, len(intervals)):
        tmp = np.concatenate((tmp, y[intervals[i][0]:intervals[i][1]]), axis=0)
    return tmp

def dataframe_to_json(data_frame, path):
    data_frame.to_json(path)