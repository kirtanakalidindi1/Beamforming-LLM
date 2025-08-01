import pyaudio
import sounddevice as sd
import numpy as np

# Method one: Get listening devices + number of channels for each connected device. The issue with this method is it only shows 
# 2 channels for the UMA 8 as opposed to 8. The only way to reconfigure it is by connecting it to a Windows device

# p = pyaudio.PyAudio()
# for i in range(p.get_device_count()):
#     info = p.get_device_info_by_index(i)
#     print(f"Device {i}: {info['name']}")
#     print(f"  Host API: {p.get_host_api_info_by_index(info['hostApi'])['name']}")
#     print(f"  Max input channels: {info['maxInputChannels']}")
#     print()


# Method two: 
#Run in the terminal : 
# ffmpeg -f avfoundation -i ":1" -ac 8 -ar 48000 -t 10 uma8_output.wav -> records all 8 channels separately.