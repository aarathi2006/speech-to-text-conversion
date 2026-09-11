# record_audio.py
import speech_recognition as sr

def record_audio(filename="recorded.wav", duration=5):
    recognizer = sr.Recognizer()
    
    # Microphone as input source
    with sr.Microphone() as source:
        print(f"Recording for {duration} seconds... Speak now!")
        recognizer.adjust_for_ambient_noise(source)  # reduce noise
        audio = recognizer.record(source, duration=duration)

    # Save to WAV
    with open(filename, "wb") as f:
        f.write(audio.get_wav_data())

    print(f"Audio saved as {filename}")

if __name__ == "__main__":
    record_audio(duration=5)

