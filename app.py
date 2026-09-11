from flask import Flask, render_template, request
import os
import base64
from transcribe import transcribe_audio

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    transcription = ""

    if request.method == "POST":

        # Case 1: user uploaded an audio file
        if "audio_file" in request.files:
            file = request.files["audio_file"]
            if file.filename != "":
                file_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(file_path)
                transcription = transcribe_audio(file_path)

        # Case 2: user recorded audio using microphone
        recorded_audio = request.form.get("recorded_audio")

        if recorded_audio:
            header, encoded = recorded_audio.split(",", 1)
            data = base64.b64decode(encoded)

            file_path = os.path.join(UPLOAD_FOLDER, "recorded_audio.webm")
            with open(file_path, "wb") as f:
                f.write(data)

            transcription = transcribe_audio(file_path)

    return render_template("index.html", text=transcription)

if __name__ == "__main__":
    app.run(debug=True)

