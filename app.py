from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import pdfplumber
from pdf2image import convert_from_path
import pytesseract
import openai
import os

# 🧠 Set OpenAI API Key (use your actual key or environment variable)
from dotenv import load_dotenv
load_dotenv()



openai.api_key = os.environ.get("OPENAI_API_KEY")


# 🚀 Initialize Flask App
app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

# 📁 Ensure uploads directory exists
if not os.path.exists('uploads'):
    os.mkdir('uploads')

# 📄 Extract text from normal PDFs
def extract_text_from_pdf(pdf_file):
    try:
        with pdfplumber.open(pdf_file) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
            return text.strip() if text else None
    except Exception as e:
        print(f"PDF Text Extraction Error: {e}")
        return None

# 🖼️ OCR: Extract text from image-based PDFs
def extract_text_from_image_pdf(pdf_file):
    try:
        images = convert_from_path(pdf_file)
        text = "\n".join([pytesseract.image_to_string(image) for image in images])
        return text.strip() if text else None
    except Exception as e:
        print(f"OCR Extraction Error: {e}")
        return None

# 🧾 Predefined Job Descriptions
def get_predefined_job_description(job_category):
    job_descriptions = {
        "Software Engineer": "Design, build, and maintain software systems using modern languages and development practices...",
        "Data Scientist": "Analyze complex datasets, create predictive models, and communicate insights using statistical and machine learning methods...",
        "Web Developer": "Develop responsive and user-friendly websites or web applications using HTML, CSS, JavaScript, and backend technologies...",
        "DevOps Engineer": "Implement CI/CD pipelines, manage cloud infrastructure, automate deployments, and monitor system performance..."
    }
    return job_descriptions.get(job_category, None)

# 🏠 Route for UI
@app.route('/')
def home():
    return render_template('index.html')

# 📤 Upload Resume + Analyze
@app.route('/analyze', methods=['POST'])
def analyze():
    job_description = request.form.get('jobDescription', '').strip()
    job_category = request.form.get('jobCategory', '').strip()
    resume_file = request.files.get('resumeUpload')

    if not resume_file:
        return jsonify({"error": "Resume file is missing."}), 400

    if not job_description and job_category:
        job_description = get_predefined_job_description(job_category)

    if not job_description:
        return jsonify({"error": "Provide either a job description or a job category."}), 400

    if resume_file.filename.split(".")[-1].lower() != "pdf":
        return jsonify({"error": "Only PDF files are supported."}), 400

    unique_filename = f"{os.urandom(16).hex()}_{resume_file.filename}"
    resume_file_path = os.path.join("uploads", unique_filename)

    try:
        resume_file.save(resume_file_path)
    except Exception as e:
        print(f"File Save Error: {e}")
        return jsonify({"error": "Could not save resume file."}), 500

    resume_text = extract_text_from_pdf(resume_file_path) or extract_text_from_image_pdf(resume_file_path)

    os.remove(resume_file_path)

    if not resume_text:
        return jsonify({"error": "Could not extract text from the resume."}), 500

    feedback = analyze_resume_with_ai(resume_text, job_description)
    return jsonify({"feedback": feedback, "status": "success"})

# 🤖 OpenAI Resume Analysis with Final Verdict
def analyze_resume_with_ai(resume_text, job_description):
    prompt = f"""
You are a professional resume analyst. Based on the following resume and job description, provide a detailed evaluation under the categories listed below. Present the response in clear bullet points under each heading.

---
📄 Resume:
{resume_text}

📌 Job Description:
{job_description}
---

### 1. 🔍 Skills Match
- Which key skills from the job description are present in the resume?
- List missing or weakly demonstrated skills.

### 2. 💼 Experience Relevance
- Evaluate how well the candidate’s past roles and responsibilities match the job requirements.
- Highlight gaps in relevant experience or domain knowledge.

### 3. ✍️ Content Optimization
- Suggest improvements in wording, clarity, and action-oriented language.
- Recommend changes to enhance structure, flow, or readability.

### 4. ⚙️ ATS Compatibility
- Assess whether the resume is ATS-friendly (keywords, formatting, layout).
- Suggest ways to improve ATS compatibility and keyword inclusion.

### 5. 📈 Strengths & Weaknesses
- Highlight strengths or notable achievements.
- List weaknesses or areas for improvement with actionable suggestions.

### 🔚 Final Verdict
- Summarize overall fit for the job in 2–3 sentences.
- Clearly state whether the candidate is a **Strong Fit**, **Moderate Fit**, or **Needs Improvement**, with reasons.
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert resume analyzer. Provide structured, helpful feedback."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.5
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        print(f"OpenAI API Error: {e}")
        return "Error analyzing the resume. Please try again later."

# 🚦 Run Server
if __name__ == '__main__':
    app.run(debug=True)
