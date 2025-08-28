from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Folder to store uploaded files
UPLOAD_FOLDER = "static/uploads"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# In-memeory "database" for now

user_data = {
    "name": "John Doe",
    "career_history": [
        {"role": "Intern", "company": "ABC Corp", "year": "2022"},
        {"role": "Junior Dev", "company": "XYZ Ltd", "year": "2023"}
    ],
    "portfolio": []
}

@app.route('/')
def profile():
    return render_template('profile.html', user=user_data)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Add uploaded file to portfolio
            user_data['portfolio'].append(filename)
            return redirect(url_for('profile'))
    return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
    

