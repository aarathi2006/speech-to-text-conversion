# speech-to-text-conversion
It easily converts the given speech into the text using the google speech recognition library.

A simple web-based **Speech-to-Text Conversion** application that converts spoken audio into text using Python and the **SpeechRecognition** library with **Google Speech Recognition**.

The application allows users to either upload an audio file or record audio through the microphone. The audio is processed and converted into readable text.

## Features

* 🎙️ Record speech using a microphone
* 📁 Upload an audio file
* 🔊 Convert speech into text
* 🤖 Uses Google Speech Recognition API through the `SpeechRecognition` Python library
* 🌐 Simple Flask-based web interface
* 📄 Displays the converted text on the webpage
* 🔄 Supports repeated audio-to-text conversion

## Technologies Used

* **Python**
* **Flask** – Backend web framework
* **SpeechRecognition** – Speech recognition library
* **Google Speech Recognition** – Speech-to-text engine
* **FFmpeg** – Audio format conversion and preprocessing
* **HTML/CSS/JavaScript** – Frontend

## Project Structure

```text
Speech-to-Text/
│
├── app.py
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   └── js/
│
├── uploads/
│
├── requirements.txt
└── README.md
```

## How the Project Works

The overall workflow is:

```text
User speaks / uploads audio
          ↓
      Flask Web App
          ↓
     Audio Processing
          ↓
   SpeechRecognition Library
          ↓
 Google Speech Recognition
          ↓
     Text Conversion
          ↓
   Display text to user
```

### Step-by-Step Process

1. The user records audio through the microphone or uploads an audio file.
2. The Flask backend receives the audio.
3. If required, **FFmpeg** is used to convert the audio into a suitable format.
4. The `SpeechRecognition` library loads the audio.
5. The audio is sent to Google's Speech Recognition service.
6. Google processes the speech and returns the recognized text.
7. The converted text is displayed on the webpage.

## Installation

### 1. Clone the Repository

```bash
git clone <your-github-repository-url>
cd Speech-to-Text
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

If you do not have a `requirements.txt` file, install the main dependencies:

```bash
pip install flask SpeechRecognition
```

For audio processing:

```bash
pip install pydub
```

### 4. Install FFmpeg

On Ubuntu:

```bash
sudo apt update
sudo apt install ffmpeg
```

Check the installation:

```bash
ffmpeg -version
```

## Running the Application

Start the Flask application:

```bash
python3 app.py
```

You should see a message similar to:

```text
Running on http://127.0.0.1:5000/
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## Requirements

Example `requirements.txt`:

```text
Flask
SpeechRecognition
pydub
```

> Note: FFmpeg is a system dependency and should be installed separately on Ubuntu/Linux.

## Speech Recognition Implementation

The main library used in this project is:

```python
import speech_recognition as sr
```

A recognizer object is created:

```python
recognizer = sr.Recognizer()
```

The audio file is loaded:

```python
with sr.AudioFile(audio_file) as source:
    audio = recognizer.record(source)
```

The recorded audio is then passed to Google's Speech Recognition service:

```python
text = recognizer.recognize_google(audio)
```

The returned value is the recognized text.

## Error Handling

The application handles common speech recognition problems such as:

### Speech Not Understood

```python
except sr.UnknownValueError:
    return "Could not understand the audio."
```

This occurs when the speech is unclear or Google cannot understand the audio.

### API / Network Error

```python
except sr.RequestError:
    return "Could not connect to the speech recognition service."
```

This can occur when there is a network problem or the Google service cannot be reached.

## Important Note

This project uses:

```python
recognizer.recognize_google(audio)
```

Therefore, the recognition process depends on **Google's online speech recognition service** and normally requires an active internet connection.

The `SpeechRecognition` library acts as a Python interface that captures/processes the audio and sends it to the selected recognition engine.

## Example

### Input

🎙️ User speaks:

> "Artificial intelligence is changing the world."

### Output

```text
Artificial intelligence is changing the world.
```

## Advantages

* Simple and easy to use
* Easy to integrate with Flask applications
* Good for prototyping speech-based applications
* Supports microphone and audio-file input
* Google Speech Recognition provides useful speech recognition accuracy for many common speech inputs

## Limitations

* Requires an internet connection when using Google's online recognition service
* Recognition accuracy can decrease with background noise
* Accents and unclear pronunciation can affect results
* Dependent on the availability of the external speech recognition service
* Not designed as a fully offline speech recognition system

## Future Improvements

Possible improvements include:

* Add support for multiple languages
* Add punctuation and formatting
* Add noise reduction before recognition
* Add speaker identification
* Store and download the generated transcripts
* Add real-time transcription
* Integrate an offline speech recognition model
* Use modern deep-learning-based ASR models such as Whisper

## Project Objective

The main objective of this project is to demonstrate how **speech can be captured as audio, processed using Python, and converted into text using a speech recognition system**.

It also demonstrates the integration of a speech-processing service with a **Flask web application**.

