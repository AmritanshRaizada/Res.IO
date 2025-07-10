
# 📄 Resume Analyzer Pro

AI-powered resume analyzer web app using Flask, OpenAI, and PDF OCR. Upload your resume and receive job-matching feedback in seconds.

---

## 🚀 Features

- Upload PDF resume (supports scanned/image-based PDFs with OCR)
- Paste a job description or use predefined job roles
- Real-time typing animation for AI feedback
- Drag-and-drop + progress bar support
- ATS-friendliness, skills match, and final verdict

---

## 📁 Project Structure

```
├── app.py                # Flask application entry point
├── .env                  # Secret keys (not tracked in Git)
├── .gitignore            # Ignored files/folders (e.g., venv, uploads)
├── render.yaml           # For deployment on Render
├── requirements.txt      # Python dependencies
├── static/               # CSS + JS
│   ├── style.css
│   └── script.js
├── templates/
│   └── index.html        # Frontend UI
├── uploads/              # Temporary file storage (auto-removed)
└── venv/                 # Virtual environment (excluded from Git)
```

---

## 🧪 Local Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/resume-analyzer-pro.git
cd resume-analyzer-pro
```

### 2. Set up virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file and add your OpenAI API key:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Run the app

```bash
python app.py
```

App will be available at `http://127.0.0.1:5000/`

---

## ☁️ Deployment (Render)

### Option 1: One-click Deploy (Recommended)

1. Push this repo to GitHub
2. Go to [https://render.com](https://render.com)
3. Click **New Web Service** → connect your repo
4. Set environment variable in dashboard:
   - `OPENAI_API_KEY` = `your-key`
5. Done 🎉

### Option 2: Use `render.yaml`

Make sure `render.yaml` is committed, then Render auto-detects config.

---

## 📦 Requirements

- Python 3.8+
- Flask
- pdfplumber
- pytesseract
- pdf2image
- openai

---

## 🛡 Security Note

Never commit your `.env` or API keys. Always use environment variables for production.

---

## 🧠 Credits

Built by [Your Name]. Powered by Flask + OpenAI + ❤️
# Res.IO
