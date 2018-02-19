"""
Main program for handling OCEANVIEW backend
Author: Chris Vantine
"""
import sys
import front
import back
import data
import database.utilities as dbutil

"""
To change the front-end, simply change the import statement.
As long as the new front-end has an init function, all should work.
"""

def main():
    """
    main function for the program
    :return: None
    """
    # Handle order: Cleardb, Testdb, front/back/both, help
    did_something = False
    if 'cleardb' in sys.argv:
        did_something = True
        print("Database Clearing not yet implemented.")

    if 'maketestdb' in sys.argv:
        did_something = True
        database = data.Database("db.sqlite", "database/build_db.sql")
        print("Adding Test Data to Database...")
        print("Adding keystrokes...")
        dbutil.add_test_data(database)
        print("Keystrokes added to test IP 127.127.127.127")
        print("Test files/screenshots not yet implemented.")

    if 'front' in sys.argv or 'both' in sys.argv:
        did_something = True
        frontend = front.init()
        frontend.run('127.0.0.1', 8000)
    if 'back' in sys.argv or 'both' in sys.argv:
        did_something = True
        backend = back.init()
        backend.run('127.0.0.1', 80)

    if did_something is False:
        print("Usage: python oceanview.py [command]")
        print("COMMANDS:")
        print("     front - start the frontend")
        print("     back - start the backend")
        print("     both - start both")
        print("     maketestdb - add test data to the database")

if __name__ == "__main__":
    main()
