from flask import Flask, render_template, request
import os
from utils.text_cleaner import clean_text
from utils.pdf_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.ats_score import calculate_ats_score

app = Flask(__name__)

# Upload folder
UPLOAD_FOLDER = '/tmp'
app.config['UPLOAD_FOLDER'] = '/tmp'

# Create uploads folder if not exists
#os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():

    if 'resume' not in request.files:
        return 'No file uploaded'

    file = request.files['resume']

    if file.filename == '':
        return 'No selected file'

    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    file.save(filepath)

    # Extract text
    resume_text = extract_text_from_pdf(filepath)
    resume_text = clean_text(resume_text)

    # Extract skills
    skills = extract_skills(resume_text)

    # Calculate ATS score
    ats_score = calculate_ats_score(skills)

    return render_template(
        'result.html',
        skills=skills,
        ats_score=ats_score,
        resume_text=resume_text
    )


if __name__ == '__main__':
    app.run(debug=True)