"""
Main program for handling OCEANVIEW backend
Author: Chris Vantine
"""
import sys
import front as front
import back
import data
import database.utilities as dbutil

# INTERFACE to listen on (global)
INTERFACE = "0.0.0.0"

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
        dbutil.add_test_data(database)

    # The user wants the front end launched
    if 'front' in sys.argv or 'both' in sys.argv:
        did_something = True
        frontend = front.init()
        frontend.run(INTERFACE, 8000)

    # The user wants the back end launched.
    if 'back' in sys.argv or 'both' in sys.argv:
        did_something = True
        backend = back.init()
        backend.run(INTERFACE, 80)

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
