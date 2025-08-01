import pyaudio
import time

# Parameters
output_raw_file = 'uma8_raw_recording_30-4-v3.raw'  # Path to save raw audio
fs = 44100
n_chans = 8 
chunk_size = 1024*8 
record_seconds = 60

# Open audio stream
p = pyaudio.PyAudio()

device_index = None
for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    if "micArray" in dev['name']:
        device_index = i
        print(f"Found UMA device at index {device_index}: {dev['name']}")
        break

if device_index is None:
    raise RuntimeError("UMA-8 microphone not found!")

stream = p.open(format=pyaudio.paInt16,
                channels=n_chans,
                rate=fs,
                input=True,
                input_device_index=device_index,
                frames_per_buffer=chunk_size)

with open(output_raw_file, 'wb') as f:
    print(f"Recording raw audio to {output_raw_file}...")
    
    try:
        while True:
            data = stream.read(chunk_size, exception_on_overflow=False)
            f.write(data)
            
    except KeyboardInterrupt:
        print("\nRecording stopped by user")

stream.stop_stream()
stream.close()
p.terminate()
print(f"Recording complete. Saved raw bytes to {output_raw_file}")
