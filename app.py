from flask import Flask, request, render_template
from pyresparser import ResumeParser
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_resume():
    if request.method == 'POST':
        resume = request.files['resume']
        filepath = os.path.join(UPLOAD_FOLDER, resume.filename)
        resume.save(filepath)
        data = ResumeParser(filepath).get_extracted_data()
        return data
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
