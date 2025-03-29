## 🎶 Music Genre Classifier

A simple machine learning web app that classifies `.wav` audio files into genres: **rock**, **jazz**, **pop**, or **classical**. It uses a CNN trained on MFCC features, with predictions served via Flask and a clean HTML frontend.

> 🧠 Model by: [@soso2910](https://github.com/soso2910)

---

### 📂 Project Structure

```
music-classifier/
├── app.py                     # Flask backend
├── templates/
│   └── index.html             # Frontend UI (served by Flask)
├── uploads/                  # Temporary folder for uploaded audio
├── music_genre_cnn_colab.h5  # ✅ Trained model (included in repo)
├── requirements.txt          # Python dependencies
├── render.yaml               # Render deploy config
└── README.md                 # You're here
```

---

### 🚀 Features

- Upload any `.wav` file via the web interface
- Predict genre in real-time using a trained CNN
- Fully local + easily deployable
- Clean beginner-friendly project structure

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

#### 4. Run the App

```bash
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

---

### 💾 Training Your Own Model (Optional)

You can train the model yourself using the included notebook. Place audio clips like this:

```
data/processed/
├── rock/rock_clip.wav
├── jazz/jazz_clip.wav
├── pop/pop_clip.wav
└── classical/classical_clip.wav
```

After training, the notebook will save:

```bash
music_genre_cnn_colab.h5
```

Include this in your repo to keep deployment simple.

---

### ☁️ Deploying on Render (Free Hosting)

1. Create a Render account at [render.com](https://render.com)
2. Push this repo to GitHub
3. Click **"New Web Service"** on Render
4. Fill in:
   - **Runtime**: Python
   - **Start command**: `python app.py`
   - **Environment**: `python`
5. Done! Your app will be live like:
   ```
   https://your-app-name.onrender.com
   ```

---

### 🛡️ .gitignore Tips

Make sure to ignore:

```gitignore
uploads/
data/
__pycache__/
venv/
```

✅ But **DO NOT** ignore `music_genre_cnn_colab.h5` now.

---

### 🙌 Credits

- Model by **[@soso2910](https://github.com/soso2910)**
- ML by **TensorFlow + Librosa**
- Backend: **Flask**
- Frontend: **HTML + JS**