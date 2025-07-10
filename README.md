# 📄 GPT Wrapper: ReS.io – AI-Powered Resume Analyzer

**ReS.io** is an intelligent resume analyzer that leverages the power of **OpenAI’s GPT-3.5** and **OCR tools** to help job seekers optimize their resumes based on specific job descriptions.

---

#LIVE LINK 
https://resio-production.up.railway.app/

## 🔍 Key Features

- **Resume Upload**: Supports both text-based and scanned (image) PDFs using `pdfplumber` and `Tesseract OCR`.
- **Job Matching**: Compares your resume against a job description to identify skill gaps, experience alignment, and ATS compatibility.
- **AI Feedback**: Uses GPT to generate detailed, categorized feedback including:
  - Skills Match ✅
  - Experience Relevance 💼
  - Content Optimization ✍️
  - ATS Compatibility ⚙️
  - Strengths & Weaknesses 📈
  - Final Verdict (Strong Fit, Moderate Fit, Needs Improvement)
- **Interactive UI**: Drag-and-drop resume upload, typing animation for feedback, and real-time progress bar.

---

## 📦 Tech Stack

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)](https://openai.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Jinja](https://img.shields.io/badge/Jinja2-B41717?style=for-the-badge&logo=jinja&logoColor=white)](https://jinja.palletsprojects.com/)
[![Tesseract](https://img.shields.io/badge/Tesseract-35495E?style=for-the-badge&logo=tesseract&logoColor=white)](https://github.com/tesseract-ocr/tesseract)
[![pdfplumber](https://img.shields.io/badge/pdfplumber-FFD43B?style=for-the-badge&logo=adobeacrobatreader&logoColor=black)](https://github.com/jsvine/pdfplumber)
[![Railway](https://img.shields.io/badge/Railway-000000?style=for-the-badge&logo=railway&logoColor=white)](https://railway.app/)

---

## 🚀 Deployment

This app can be deployed on platforms like **Render** or **Vercel**. For Render, use a `render.yaml` and set your OpenAI API key in the dashboard as an environment variable.

For Vercel:
- Deploy frontend separately (if needed)
- Use Vercel functions for backend (Flask via `vercel-python` builder) or connect to an external Flask server

Make sure your `.env` or environment variables include:

```bash
OPENAI_API_KEY=your_openai_key_here
```

---

## 📂 Folder Structure (Typical)

```
.
├── static/
│   ├── style.css
├── templates/
│   ├── index.html
├── uploads/
├── app.py
├── requirements.txt
├── README.md
```

---

## 🙌 Contribution

Feel free to fork the repository and open pull requests for improvements.

---

## 📬 Contact

Built with ❤️ by Amritansh Raizada .  
Feel free to reach out via amritanshspc@gmail.com.
