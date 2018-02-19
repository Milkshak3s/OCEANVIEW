"""
Main program for handling OCEANVIEW backend
Author: Chris Vantine
"""
import sys
from flask import Flask
import front
import back
import data

def main():
    """
    main function for the program
    :return: None
    """
    if 'front' in sys.argv or 'both' in sys.argv or 'back' in sys.argv:
        app = Flask(__name__)
        app.config['UPLOAD_FOLDER'] = 'uploads/'
        app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg'}
        database = data.Database("db.sqlite", "database/build_db.sql")
        if 'front' in sys.argv or 'both' in sys.argv:
            front.init(app)
        if 'back' in sys.argv or 'both' in sys.argv:
            back.init(app, database)
        app.run(host='127.0.0.1', port=80)
    elif 'maketestdb' in sys.argv or 'cleardb' in sys.argv:
        print("Database commands not yet implemented.")
    else:
        print("No Action Specified")

if __name__ == "__main__":
    main()
