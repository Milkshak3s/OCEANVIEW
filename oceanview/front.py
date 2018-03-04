"""
show what's in OCEANVIEW's database.
author: Ethan Witherington.
"""

import html
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
        return render_template('index.html')

    # Warning on except; no exception types specified. Noted. Thanks pep8.
    # pylint: disable=W0702
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
        Handle a JSON request sent by the client.
        Should include a type and optionally some data.
        """
        # Make sure it's JSON
        if not request.is_json:
            print("data request was not JSON.")
            abort(400)
        json = request.get_json()
        # Make sure the type is specified.
        if not 'type' in json:
            print("data request did not include a type")
            abort(400)
        # Handle a Text Update request
        if json['type'] == 'text':
            # Make sure we have a since and addr field
            if not 'since' in json:
                print("data request did not include a since")
                abort(400)
            if not 'addr' in json:
                print("data request did not include an ip address.")
                abort(400)
            return jsonify(get_text(json['since'], json['addr'], database))
        # Handle an IP and TAG request.
        if json['type'] == 'ip':
            return jsonify(get_ips(database))
        if json['type'] == 'addtag':
            if not 'addr' in json:
                print("addtag request did not include an address")
                abort(400)
            if not 'tag' in json:
                print("addtag request did not include a tag.")
                abort(400)
            database.add_tag(addr=json['addr'], tag=json['tag'])
            return ('', 204) # http status code no content
        if json['type'] == 'rmtag':
            if not 'addr' in json:
                print("rmtag request did not include an address")
                abort(400)
            if not 'tag' in json:
                print("rmtag request did not include a tag.")
                abort(400)
            database.remove_tag(addr=json['addr'], tag=json['tag'])
            return ('', 204) # http status code no content
        # The request did not match any types that we handle.
        print("The following request is incorrect:")
        print(json)
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
        parsed.append(html.escape(entry[1]))
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


def get_ips(database):
    """Return all IP addresses in the DB with Tags"""
    hosts = database.get_unique_hosts()
    """
    database.get_unique_hosts returns:
    [
        'ip1',
        'ip2'
    ]
    """
    final = []
    for host in hosts:
        obj = {}
        obj["ip"] = host
        obj["tags"] = []
        tags = database.get_tags(host)
        """
        database.get_tags(host) returns:
        [
            'testing',
            'guac',
            'guacamole.'
        ]
        """
        for tag in tags:
            obj["tags"].append(tag)
        final.append(obj)
    return final
