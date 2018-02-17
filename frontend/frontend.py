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

<<<<<<< HEAD
@APP.route('/overview/<string:addr>')
def machine(addr='192.168.420.69'):
    """Show info about a specific machine"""
    return render_template('overview.html', addr=addr)
=======
@APP.route('/machine/<string>')
def machine(string='guac'):
    """Show info about a specific machine"""
    return render_template('ip.html', string=string)
>>>>>>> Chris says I have to commit.
