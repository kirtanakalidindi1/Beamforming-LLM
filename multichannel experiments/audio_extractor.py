##Splits the multichannel audio into individual channels and stores each channel as a separate .wav file
import soundfile as sf
import os

def split_and_save_channels(input_wav_path, output_dir):
    # Load the multichannel audio
    audio_data, fs = sf.read(input_wav_path)
    
    os.makedirs(output_dir, exist_ok=True)

    num_channels = audio_data.shape[1]
    
    for ch in range(num_channels):
        channel_data = audio_data[:, ch]
        output_path = os.path.join(output_dir, f"channel_{ch + 1}.wav")
        sf.write(output_path, channel_data, fs)
        print(f"Saved channel {ch + 1} to {output_path}")

split_and_save_channels('uma8_output.wav', 'extracted_channels/')
