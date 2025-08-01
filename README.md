# Beamforming-LLM: Semantic Recall in Multi-Speaker Environments

This project implements a real-time spatial audio recall system that combines automatic speech recognition (Whisper), semantic search (FAISS), and GPT-4o-mini summarization to extract and summarize relevant content from multi-speaker conversations.

Developed as part of a collaborative research project at Columbia University with Swetha Ramesh and Vishal Chaudhari, the system simulates complex acoustic environments using beamforming filters and provides a natural language interface for semantic audio retrieval.

## Features
- Real-time directional audio separation using microphone array and Pyroomacoustics
- Whisper-based ASR for transcription of overlapping conversations
- FAISS + RAG pipeline for semantic search and GPT-4o-mini summarization
- Streamlit demo interface and Raspberry Pi deployment simulation




# ELENE6908_group5
Repo for the Embedded AI project 

Project Plan for Beamforming-LLM Project


Goal: Have a system that can record multiple conversations in a place. Say, you are with your friends at a restaurant. Clusters of conversations get formed and it is impossible to take part in each conversation. With the help of this device, anyone who was at the dinner can query the device and ask questions like- “What did I miss when I was following the conversation on dogs?” And the device would tell you- “There were two other conversations and one of them was on Persian food and the other was a friend discussing his later trip to Europe”.

You can also use it to recall conversations you were a part of at the end of the day in a NOISELESS, INTERFERENCE-FREE ENVIRONMENT which is the basic memory recall device.

The goal is to have spatial understanding and have a natural language interface which can summarize things that you missed while you were engaged in another conversation.

First priority:
To achieve this, there are two major components.

Beamforming:
The beamformer microphone records multi-channel audio.
Spatial filtering is applied to separate out the sound sources (libraries, video tutorials should be available).
So, the output data format would be a dictionary of .wav files from a long multi-conversation recording
separatedOutputs = {‘left’: xyz.wav, ‘front’: abc.wav, ‘back’: mno.wav.} 

LLM-RAG:
These conversations need to be transcribed with timestamps.
Then, these need to be jointly embedded in a vector storage, along with timestamps.
Once the user enters a query, the query also needs to be encoded.
This encoded query is used to find closest vectors, which are then retrieved.
The LLM then condenses the retrieved vectors in natural language.
It may also yield time stamps which can then be used to chop relevant snippets in the recordings of individual conversations.
Fine-tuning of the LLM and/or configure of the vector database may be needed.


Second priority:
Eventually, for a product, we need to think of making it work in a real-time manner (without working with offline recordings but rather incoming online live streams of audio) as well as work on privacy, all of which are very important.


Libraries to install:
1. pip install pyaudio
2. pip install soundfile
2. brew install portaudio

The source for the audio_streaming_python_repo can be found here : https://github.com/thomeou/audio_streaming_using_pyaudio/tree/master?tab=readme-ov-file

