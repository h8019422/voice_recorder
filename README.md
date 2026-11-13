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

#### Notice
- PyAudio is not supported by Python versoin newer than v.3.13, so Use PyAudioWPatch is the easiest for Python 3.15
- 2026/11/13 中文化
- 2026/11/12 .env 重建

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

### to create exe
activate .env
```
.\.venv\Scripts\Activate.ps1 
```

```
python -m PyInstaller --clean --onefile --icon=.\recorder.ico --noconsole --name="recorder_mp3.exe" "recorder_mp3.py" 
python -m PyInstaller --clean --onefile --noconsole --name="recorder_mp3.exe" "recorder_mp3.py"
```
確認環境無誤後，建議加上清除快取的參數來重新編譯，避免舊的打包紀錄干擾。
• 執行打包指令。 輸入 `python -m PyInstaller --onefile --clean recorder_mp3.py`（使用 python -m PyInstaller 可以 100% 確保呼叫的是目前 .venv 內的 PyInstaller）。
• 強制收集隱藏模組（若仍報錯）。 如果執行新生成的 .exe 依然提示找不到 pyaudio，請改用 `python -m PyInstaller --onefile --clean --collect-all pyaudio recorder_mp3.py` 強制將所有相關檔案封裝進去。

Python 的 python -m 指令對大小寫非常敏感，因此 Pyinstaller（小寫 i）會找不到模組。
• 執行正確指令。 注意 PyInstaller 的 P 與 I 皆為大寫：
python -m PyInstaller --onefile --clean recorder_mp3.py

如果你的程式是透過 pydub 呼叫 ffmpeg 來輸出 MP3，打包成 .exe 後有幾點需要注意：
• 放入 ffmpeg.exe。 pyinstaller 不會自動打包外部系統程式，你必須將 ffmpeg.exe 放在生成的 dist\recorder_mp3.exe 旁邊（同一個資料夾），或是使用 --add-binary "ffmpeg.exe;." 參數一起打包。
• 保留終端機視窗除錯。 測試階段請先不要加上 --noconsole 或 -w 參數，並建議從 PowerShell 執行 .\dist\recorder_mp3.exe，這樣萬一程式閃退才能看到完整的錯誤訊息。
