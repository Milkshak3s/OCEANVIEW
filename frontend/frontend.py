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

@APP.route('/machine/<string>')
def machine(string='guac'):
    """Show info about a specific machine"""
    return render_template('ip.html', string=string)
