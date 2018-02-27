"""
Various functions that are required by other modules
Author: Micah Martin
"""

import time

TEST_TEXT = [
    "Never",
    "Gonna",
    "Give",
    "You",
    "Up",
    "This line is very very long, so that the web dev person can make sure\
    that stupid long lines don't break the frontend UI.",
    "rm -rf /*",
    "There is no need to be concerned"
]


# pylint: disable=W0702
def validate_ip(addr):
    """
    Validate that an IP address is legitimate
    """
    # Changing how hosts are identified
    """
    try:
        vals = [(int(i) < 256) for i in addr.split(".")]
        vals += [len(vals) == 4]
        return all(vals)
    except:
        return False
    """
    return True

def add_test_data(database):
    """ Put test data into the database """
    for stringy in TEST_TEXT:
        database.add_keystroke(addr='127.127.127.127', keystroke=stringy)
        time.sleep(1)
