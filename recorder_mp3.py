import tkinter as tk
from turtle import left
#  import pyaudiowpatch as pyaudio
import pyaudio
import lameenc
import threading
import os

class App:
    def __init__(self, master):
        self.is_recording = False
        self.filename = "output.mp3"
        self.record_button = tk.Button(master, text="開始錄音", font=("Microsoft YaHei", 14), bg="lightgreen", command=self.start_recording)
        self.record_button.pack(padx=10, pady=10)
        self.stop_button = tk.Button(master, text="停止錄音", font=("Microsoft YaHei", 14), bg="yellow", command=self.stop_recording, state="disabled")
        self.stop_button.pack(padx=10, pady=10)
        self.label = tk.Label(master, text="提醒:\n1.錄音文件將保存在.\\audio_files\\output.mp3" \
        "\n2.若錄音文件已存在,將自動生成唯一文件名,如output_1.mp3,output_2.mp3等 " \
        "\n3.此程式為mp3格式錄音器", font=("Microsoft YaHei", 10), justify="left") 
        self.label.pack(padx=10, pady=10, anchor="w")

    def create_output_directory(self):
        directory = "audio_files"
        if not os.path.exists(directory):
            os.makedirs(directory)


    def start_recording(self):
        self.is_recording = True
        self.record_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.record_audio()

    def stop_recording(self):
        self.is_recording = False
        self.record_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def get_unique_filename(self, base_filename):
        directory = "audio_files"
        counter = 1
        unique_filename = os.path.join(directory, base_filename)
        base_name, extension = os.path.splitext(base_filename)

        while os.path.exists(unique_filename):
            unique_filename = os.path.join(directory, f"{base_name}_{counter}{extension}")
            counter += 1

        return unique_filename

    def record_audio(self):
        self.create_output_directory()
        CHUNK = 1024
        FORMAT = pyaudio.paInt16
        CHANNELS = 1
        RATE = 44100

        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

        frames = []

        def _record():
            while self.is_recording:
                data = stream.read(CHUNK)
                frames.append(data)

            stream.stop_stream()
            stream.close()
            p.terminate()

            unique_filename = self.get_unique_filename(self.filename)
            encoder = lameenc.Encoder()
            encoder.set_bit_rate(128)
            encoder.set_in_sample_rate(RATE)
            encoder.set_channels(CHANNELS)
            encoder.set_quality(2)

            with open(unique_filename, "wb") as mp3_file:
                for frame in frames:
                    mp3_file.write(encoder.encode(frame))
                mp3_file.write(encoder.flush())

        threading.Thread(target=_record).start()

root = tk.Tk()
root.iconbitmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), "recorder.ico"))
#root.geometry("500x200")
root.title("錄音小程式 v1.0")
app = App(root)
root.mainloop()
