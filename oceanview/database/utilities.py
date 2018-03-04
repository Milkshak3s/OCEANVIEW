"""
Various functions that are required by other modules
Author: Micah Martin
"""

TEST_TEXT = [
    b"<5p3c1@l> Chars work &<|>",
    b"This text data was inserted by passing OCEANVIEW the 'maketestdb' command.",
    b"This is a Test IP."
]

TEST_IPS = [
    "127.0.0.2",
    "127.0.0.3",
    "127.0.0.4",
    "127.0.0.5",
    "127.0.0.6",
    "127.0.0.7",
    "127.0.0.8",
    "127.0.0.9",
    "127.0.0.10",
    "127.0.0.11",
    "127.0.0.12",
    "127.0.0.13",
    "127.0.0.14",
    "127.0.0.15",
    "127.0.0.16",
    "127.0.0.17",
    "127.0.0.18",
    "127.0.0.19",
    "127.0.0.20",
    "127.0.0.21",
    "127.0.0.22",
    "127.0.0.23",
    "127.0.0.24",
    "127.0.0.25",
    "127.0.0.26",
    "127.0.0.27",
    "127.0.0.28",
    "127.0.0.29",
    "127.0.0.30",
    "127.0.0.31",
    "127.0.0.32",
    "127.0.0.33",
    "127.0.0.34",
    "127.0.0.35",
    "127.0.0.36",
    "127.0.0.37",
    "127.0.0.38",
    "127.0.0.39",
    "127.0.0.40",
    "127.0.0.41",
    "127.0.0.42",
    "127.0.0.43",
    "127.0.0.44",
    "127.0.0.45",
    "127.0.0.46",
    "127.0.0.47",
    "127.0.0.48",
    "127.0.0.49",
    "127.0.0.50"
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
    for ip in TEST_IPS: # pylint: disable=C0103
        database.add_file(ip, 'static/dog.jpg')
        database.add_tag(ip, "test")
        for text in TEST_TEXT:
            database.add_keystroke(ip, text)
    print("Test Data Added.")
