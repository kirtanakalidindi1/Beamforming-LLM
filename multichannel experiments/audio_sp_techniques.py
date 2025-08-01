## This code applies basic signal processing techniques on the .wav file. Requires more experimentation
# This code was used to see how we could apply signal processing but requires more fine-tuning in terms of what we could use 

import wave
import numpy as np
import soundfile as sf
from scipy.signal import butter, sosfilt, windows

w_in = '/Users/srs/audio_streaming_using_pyaudio/uma8_2025_04_17_18_38_58.wav'
w_out = '/Users/srs/audio_streaming_using_pyaudio/test_audio.wav'

# print("Channels:", w_in.getnchannels())
# print("Sample rate:", w_in.getframerate())

def remove_dc_offset(signal):
    return signal - np.mean(signal, axis=0, keepdims=True)

def normalize(signal):
    max_val = np.max(np.abs(signal), axis=0, keepdims=True)
    return signal / (max_val + 1e-6)

def apply_hamming_window(signal):
    window = windows.hamming(signal.shape[0])
    return signal * window[:, np.newaxis]

def bandpass_filter(signal, fs, lowcut=300, highcut=3400, order=5):
    sos = butter(order, [lowcut, highcut], btype='bandpass', fs=fs, output='sos')
    return sosfilt(sos, signal, axis=0)

# Main preprocessing function
def preprocess_multichannel_wav(input_wav_path, output_wav_path):
    audio_data, fs = sf.read(input_wav_path)  # shape: (samples, channels)

    # Preprocessing
    cleaned = remove_dc_offset(audio_data)
    normalized = normalize(cleaned)
    windowed = apply_hamming_window(normalized)
    filtered = bandpass_filter(windowed, fs)

    # Save to output file
    sf.write(output_wav_path, filtered, fs)
    print(f"Saved processed audio to: {output_wav_path}")


processed_audio = preprocess_multichannel_wav(w_in, w_out)
print(processed_audio)

