"""
Main program for handling OCEANVIEW backend
Author: Chris Vantine
"""
import sys
import front as front
import back
import data
import database.utilities as dbutil

"""
    To Change the Font-end:
        Make sure the new front end has an 'init' function that returns a flask app.
        change the above import line from

            import front as front

        to

            import newfront as front

        where newfront is whatever the new frontend is called.
"""

def main():
    """
    main function for the program
    :return: None
    """

    # Has oceanview done something? If this is still false by the end,
    # Display the Usage information.
    did_something = False

    # The user wants to clear the database.
    if 'cleardb' in sys.argv:
        did_something = True
        print("It's sqlite, just delete the file.")

    # The user wants the test data added to the database.
    if 'maketestdb' in sys.argv:
        did_something = True
        database = data.Database("db.sqlite", "database/build_db.sql")
        print("Adding Test Data to Database...")
        print("Adding keystrokes...")
        dbutil.add_test_data(database)
        print("Keystrokes added to test IP 127.127.127.127")
        print("Test files/screenshots not yet implemented.")

    # The user wants the front end launched
    if 'front' in sys.argv or 'both' in sys.argv:
        did_something = True
        frontend = front.init()
        frontend.run('127.0.0.1', 8000)

    # The user wants the back end launched.
    if 'back' in sys.argv or 'both' in sys.argv:
        did_something = True
        backend = back.init()
        backend.run('127.0.0.1', 80)

    # did_something is False, nothing was done, show the usage info.
    if did_something is False:
        print("Usage: python oceanview.py [command]")
        print("COMMANDS:")
        print("     front - start the frontend")
        print("     back - start the backend")
        print("     both - start both")
        print("     maketestdb - add test data to the database")

if __name__ == "__main__":
    main()
