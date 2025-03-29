from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import librosa
import numpy as np
from tensorflow.keras.models import load_model
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

model = load_model("music_genre_cnn_colab.h5")
GENRE_LIST = ['rock', 'jazz', 'pop', 'classical']

@app.route("/")
def home():
    return render_template("index.html")  # ← serves your frontend

@app.route("/predict-genre", methods=["POST"])
def predict_genre():
    if "audio" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["audio"]
    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    file.save(filepath)

    def extract_mfcc(file_path, max_len=130):
        y, sr = librosa.load(file_path, sr=22050, mono=True)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
        if mfcc.shape[1] < max_len:
            mfcc = np.pad(mfcc, pad_width=((0, 0), (0, max_len - mfcc.shape[1])), mode="constant")
        else:
            mfcc = mfcc[:, :max_len]
        return mfcc

    mfcc = extract_mfcc(filepath)
    input_mfcc = np.expand_dims(mfcc, axis=(0, -1))
    prediction = model.predict(input_mfcc)
    predicted_label = int(np.argmax(prediction))
    predicted_genre = GENRE_LIST[predicted_label]

    return jsonify({"genre": predicted_genre})

if __name__ == "__main__":
    app.run(debug=True)
