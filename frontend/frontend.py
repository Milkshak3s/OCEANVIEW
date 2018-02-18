"""
Make OCEANVIEW's backend easy to use.
author: Ethan Witherington.
"""

from flask import Flask
from flask import render_template
APP = Flask(__name__)

@APP.route('/')
def index():
    """Show my pretty index.html file"""
    return render_template('index.html')

@APP.route('/overview/<string:addr>')
def machine(addr='192.168.420.69'):
    """Show info about a specific machine"""
    # Firstly, validate the IP.
    if validate_ip(addr):
        return render_template('overview.html', addr=addr)
    return "Invalid IP. You're BAD and you should feel BAD."

def validate_ip(_addr):
    """Tell if an IP is a valid IP."""
    return True
