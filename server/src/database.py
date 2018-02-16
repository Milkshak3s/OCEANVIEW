"""
Database handler object
Author: Micah Martin (knif3)
"""

from os.path import exists
import sqlite3
class Database(object):
    """
    Database handler object. Abstracts alot of SQLite stuff
    """
    def __init__(self, location):
        # The location of the DB
        self.location = location
        # If it exists, get all the tables
        if exists(location):
            self.conn = sqlite3.connect(location, check_same_thread=False)
            self.cur = self.conn.cursor()
        else:
            raise Exception("Database not found {}.".format(location))

    def create(self, script=None):
        '''
        Create the database with the given script
        '''
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
        db_connection.commit()
    
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def close(self):
        """
        Close the connection
        """
        self.conn.close()

    def handle_query(self, qry, value):
        """
        Handle one specific query where there is only one value
        """
        if type(value).__name__ in ('str', 'int'):
            value = (value,)
        self.cur.execute(qry, value)
        return self.newcur(self.cur)

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

