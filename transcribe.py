import speech_recognition as sr
import subprocess
import os

def convert_to_wav(input_path):
    wav_path = input_path.rsplit(".", 1)[0] + ".wav"

    command = [
        "ffmpeg",
        "-y",
        "-i", input_path,
        "-ar", "16000",
        "-ac", "1",
        wav_path
    ]

    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return wav_path


def transcribe_audio(file_path):
    wav_file = convert_to_wav(file_path)

    recognizer = sr.Recognizer()

    with sr.AudioFile(wav_file) as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except Exception:
        return "Could not transcribe audio."

