"""
filename:       server.py
program:        OCEANVIEW

description:    A platform for tracking blue team activity

author:         Chris Vantine
"""
import os
from flask import Flask
from werkzeug.utils import secure_filename
app = Flask(__name__)

# set upload settings
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg'])

@app.route("/upload", methods=['POST'])
def file_upload():
    """
    upload a file

    :return: "invalid" if file invalid, "success" if upload successful
    """
    try:
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "success"
        return "invalid"
    except:
        return "invalid"