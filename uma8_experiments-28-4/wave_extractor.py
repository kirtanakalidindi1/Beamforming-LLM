import numpy as np
import wave
import os

# Parameters
input_raw_file = 'uma8_raw_recording_30-4-v3.raw' 
output_dir = 'extracted_channels'
n_channels = 8

os.makedirs(output_dir, exist_ok=True)

with open(input_raw_file, 'rb') as f:
    raw_data = f.read()

audio_data = np.frombuffer(raw_data, dtype=np.int16)

if len(audio_data) % n_channels != 0:
    raise ValueError(f"Raw audio data length ({len(audio_data)}) is not divisible by the number of channels ({n_channels}).")

audio_data = audio_data.reshape(-1, n_channels)

def save_wav(filename, audio_data, sample_rate=44100):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2) 
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())

for ch in range(n_channels):
    channel_data = audio_data[:, ch]
    save_wav(os.path.join(output_dir, f'channel_{ch + 1}.wav'), channel_data)

print(f"All {n_channels} channels saved to {output_dir}")
