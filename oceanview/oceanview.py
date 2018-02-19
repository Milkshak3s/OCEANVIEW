"""
Main program for handling OCEANVIEW backend
Author: Chris Vantine
"""
import sys
import time
from flask import Flask
import front
import back
import data

def main():
    """
    main function for the program
    :return: None
    """
    database = data.Database("db.sqlite", "database/build_db.sql")
    if 'front' in sys.argv or 'both' in sys.argv or 'back' in sys.argv:
        app = Flask(__name__)
        app.config['UPLOAD_FOLDER'] = 'uploads/'
        app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg'}
        if 'front' in sys.argv or 'both' in sys.argv:
            front.init(app, database)
        if 'back' in sys.argv or 'both' in sys.argv:
            back.init(app, database)
        app.run(host='127.0.0.1', port=80)
    elif 'maketestdb' in sys.argv or 'cleardb' in sys.argv:
        if 'maketestdb' in sys.argv:
            print("Adding Test Data to Database...")
            print("Adding keystrokes...")
            strokes = [
                "Never",
                "Gonna",
                "Give",
                "You",
                "Up",
                "This line is very very long, so that the web dev person can make sure\
                that stupid long lines don't break the frontend UI.",
                "rm -rf /*",
                "There is no need to be concerned"
            ]
            for stringy in strokes:
                database.add_keystroke(addr='127.127.127.127', keystroke=stringy)
                time.sleep(1)
            print("Keystrokes added to test IP 127.127.127.127")
            print("Test files/screenshots not yet implemented.")
        else:
            print("Database Clearing not yet implemented.")
    else:
        print("Usage: python oceanview.py [command]")
        print("COMMANDS:")
        print("     front - start the frontend")
        print("     back - start the backend")
        print("     both - start both")
        print("     maketestdb - add test data to the database")

if __name__ == "__main__":
    main()
