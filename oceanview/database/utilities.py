"""
Various functions that are required by other modules
Author: Micah Martin
"""

import time

TEST_TEXT = [
    b"<LeftShiftDown>N<LeftShiftUp>ever",
    b"Gonna",
    b"Give",
    b"You",
    b"Up",
    b"This line is very very long, so that the web dev person can make sure\
    that stupid long lines don't break the frontend UI.",
    b"rm -rf /*",
    b"There is no need to be concerned",
    b"LOOK AT THE HAPPY DOG, JOE."
]


# pylint: disable=W0702, W0613
def validate_ip(addr): # W0613 suppresses addr not used warning.
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
    print("Adding fake keystrokes...")
    for stringy in TEST_TEXT:
        database.add_keystroke(addr='127.127.127.127', keystroke=stringy)
        time.sleep(1)
    print("Adding fake images...")
    database.add_file(addr='127.127.127.127', filename='static/wave.jpg')
    time.sleep(1)
    database.add_file(addr='127.127.127.127', filename='static/dog.jpg')
    print("Adding Tags to test IP...")
    database.add_tag("127.127.127.127", "testing")
    time.sleep(1)
    database.add_tag("127.127.127.127", "guac")
    time.sleep(1)
    database.add_tag("127.127.127.127", "guacamole.")
    print("Adding tags to more IPs...")
    database.add_tag("127.127.127.0", "guacamole.")
    time.sleep(1)
    database.add_tag("127.127.127.1", "guacamole.")
    time.sleep(1)
    database.add_tag("127.127.127.2", "guacamole.")
    time.sleep(1)
    database.add_tag("127.127.127.3", "guacamole.")
    time.sleep(1)
    database.add_tag("127.127.127.4", "guacamole.")
    time.sleep(1)
    database.add_tag("127.127.127.5", "guacamole.")
    time.sleep(1)
    database.add_tag("127.127.127.6", "guacamole.")
    time.sleep(1)
    database.add_tag("127.127.127.7", "guacamole.")
    time.sleep(1)
    database.add_tag("127.127.127.8", "guacamole.")
    time.sleep(1)
    database.add_tag("127.127.127.9", "guacamole.")
    time.sleep(1)
    database.add_tag("127.127.127.10", "guacamole.")
    time.sleep(1)
    print("Test Data Added.")
