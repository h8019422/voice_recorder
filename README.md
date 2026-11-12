# voice_recorder
Simple voice recorder that uses your default microphone to record MP3 audio and output it to a folder called ```audio_files```

## How to use it
#### EXE
There is an exe version of it in the releases area, just go to the following link and download the exe file: https://github.com/JarodMica/voice_recorder/releases

If you're using the exe, your anti-virus may block it due to being an unknown exe file, you just have to allow it or use the python script version of it.

#### Python
Clone the repo with:

```git clone https://github.com/JarodMica/voice_recorder.git```

Once you have done that, navigate into the folder and install requirements.  I recommend you use a venv if you're familiar with them to prevent any package issues later on:
```
cd voice_recorder
pip install -r requirements.txt
```

Now that you have all the requirements, you should be able to just run the script either by using an IDE or by CMD with the following command (as long as you're in the voice_recorder folder path):
```python voice_recorder.py```

PyAudio is not supported by Python versoin newer than v.3.13
so Use PyAudioWPatch is the easiest for Python 3.15

PyAudioWPatch is a maintained drop-in replacement for PyAudio on Windows that provides pre-built wheels for Python 3.15 out of the box. It includes all standard PyAudio functions plus support for recording system audio (WASAPI loopback).
• Install the package. Run 
```
pip install PyAudioWPatch
```
 in your .venv terminal.
 
• Update your import line. Change your import statement in your Python script to 
```
import pyaudiowpatch as pyaudio
```
All your existing pyaudio.PyAudio() and stream code will work without changes.