"""
Base tests for pytest integration
Author: Chris Vantine
"""
from multiprocessing import Process
from oceanview import *
import oceanview.front as front
import oceanview.back as back
import oceanview.data as data
import oceanview.database.utilities as dbutil
import oceanview.utilities.pwnboard as pwnboard

# Interface to listen on (localhost for testing)
INTERFACE = "127.0.0.1"


def test_dbsetup():
    database = data.Database("db.sqlite", "/home/travis/build/Milkshak3s/OCEANVIEW/oceanview/database/build_db.sql")
    dbutil.add_test_data(database)


def test_front_init():
    frontend = front.init()
    server = Process(target=frontend.run, args=(INTERFACE, 8000))
    server.start()
    server.terminate()
    server.join()


def test_back_init():
    backend = back.init()
    server=Process(target=backend.run, args=(INTERFACE, 80))
    server.start()
    server.terminate()
    server.join()

def test_utility_pwnboard():
    pwnboard.sendUpdate("10.0.0.1")