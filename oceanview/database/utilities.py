"""
Various functions that are required by other modules
Author: Micah Martin
"""

import time

TEST_TEXT = [
    b"<5p3c1@l> Chars work &<|>",
    b"This text data was inserted by passing OCEANVIEW the 'maketestdb' command.",
    b"This is a Test IP."
]

TEST_IPS = [
    "127.0.0.2",
    "127.0.0.3",
    "127.0.0.4"
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
    print("Adding test data...")
    for text in TEST_TEXT:
        for ip in TEST_IPS: # pylint: disable=C0103
            database.add_keystroke(ip, text)
            database.add_file(ip, 'static/dog.jpg')
            database.add_tag(ip, "test")
    print("Test Data Added.")
