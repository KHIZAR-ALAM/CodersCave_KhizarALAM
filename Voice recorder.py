import tkinter as tk
import pyaudio
import wave
import os
import threading
from tkinter import simpledialog

p = pyaudio.PyAudio()

class VoiceRecorderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Recorder")

        self.record_button = tk.Button(root, text="Record", command=self.start_recording)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_recording)
        self.play_button = tk.Button(root, text="Play", command=self.play_recording)
        self.save_button = tk.Button(root, text="Save", command=self.save_recording)

        self.record_button.pack()
        self.stop_button.pack()
        self.play_button.pack()
        self.save_button.pack()

        self.frames = []
        self.recording = False
        self.stream = None
        self.p = pyaudio.PyAudio()

    def start_recording(self):
        self.frames = []
        self.recording = True
        self.record_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.play_button.config(state="disabled")
        self.save_button.config(state="disabled")

        self.stream = self.p.open(format=pyaudio.paInt16,
                                  channels=2,
                                  rate=44100,
                                  input=True,
                                  frames_per_buffer=1024)

        self.record_thread = threading.Thread(target=self.audio_callback)
        self.record_thread.start()

    def audio_callback(self):
        while self.recording:
            data = self.stream.read(1024)
            self.frames.append(data)

    def stop_recording(self):
        self.recording = False
        self.record_thread.join()
        self.stream.stop_stream()
        self.stream.close()
        self.record_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.play_button.config(state="normal")
        self.save_button.config(state="normal")

    def play_recording(self):
        if len(self.frames) > 0:
            self.p.open(format=pyaudio.paInt16,
                        channels=2,
                        rate=44100,
                        output=True)
            for frame in self.frames:
                self.p.write(frame)
            self.p.close()

    def save_recording(self):
        if len(self.frames) > 0:
            filename = simpledialog.askstring("Input", "Enter a filename for the recording (without extension):")
            if filename:
                filename += ".wav"
                wf = wave.open(filename, "wb")
                wf.setnchannels(2)
                wf.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
                wf.setframerate(44100)
                wf.writeframes(b"".join(self.frames))
                wf.close()
                print(f"Recording saved as {filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceRecorderApp(root)
    root.mainloop()
