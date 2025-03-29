## 🎶 Music Genre Classifier

This is a simple machine learning project that classifies music into genres based on `.wav` audio input. It uses a CNN trained on MFCC features extracted from audio clips and serves predictions through a Flask backend with an HTML frontend.

---

### 📂 Project Structure

```
music-classifier/
├── app.py                     # Flask backend
├── templates/
│   └── index.html             # Frontend (served by Flask)
├── uploads/                  # Temporary folder for uploaded audio
├── music_genre_cnn_colab.h5  # Trained model (not included in repo)
├── data/                     # Local training audio clips (not included)
├── requirements.txt          # Dependencies
└── README.md                 # You are here
```

---

### 🚀 Features

- Upload a `.wav` audio file
- Predicts one of 4 genres: **rock**, **jazz**, **pop**, **classical**
- Trained using **MFCC features** + **CNN model**
- Web interface via HTML & Flask

---

### 🧠 How It Works

1. Audio features are extracted using **Librosa**.
2. A **CNN** classifies the genre based on MFCCs.
3. The Flask backend handles prediction and the frontend file upload.

---

### 🔧 How to Run Locally

#### 1. Clone the Repo

```bash
git clone https://github.com/nonvegetable/music-classifier.git
cd music-classifier
```

#### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Make Sure the Model is Present

The file `music_genre_cnn_colab.h5` must exist.  
If not, [train it using this notebook](#training-your-model).

#### 5. Run the Server

```bash
python app.py
```

Then visit `http://127.0.0.1:5000/` in your browser.

---

### 💾 Training Your Model

You can train the model using your own `.wav` files by following the instructions in the included Jupyter notebook. Expected structure:

```
data/processed/
├── rock/rock_clip.wav
├── jazz/jazz_clip.wav
├── pop/pop_clip.wav
└── classical/classical_clip.wav
```

After training, the model will be saved as:

```bash
music_genre_cnn_colab.h5
```

---

### 📦 Dependencies

All Python dependencies are listed in `requirements.txt`, including:

- Flask
- TensorFlow / Keras
- Librosa
- NumPy
- Scikit-learn
- Werkzeug

---

### 🛡️ .gitignore Suggestions

Make sure to exclude:
- `uploads/` folder
- `music_genre_cnn_colab.h5`
- `data/`
- Virtual environments (`venv/`)

---

### 🌟 Future Improvements

- Add support for more genres
- Use larger dataset
- Add drag-and-drop file upload
- Show waveform or spectrogram
- Deploy online (Render, Replit, etc.)

---

### 🤝 Credits

Created as a fun ML + Web integration project.  
Trained using `.wav` files and powered by TensorFlow and Flask.

---
### 🙌 Shoutout

Huge thanks to @soso2910 for creating the original training model used in this project! 🎉