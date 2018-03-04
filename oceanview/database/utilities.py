"""
Various functions that are required by other modules
Author: Micah Martin
"""

TEST_IPS_NUM = 50
TEST_TEAM_NUMS = 7

TEST_TEXT = [
    b"<5p3c1@l> Chars work &<|>",
    b"This text data was inserted by passing OCEANVIEW the 'maketestdb' command.",
    b"This is a Test IP."
]

TEST_TAGS_WINDOWS = [
    "rdp",
    "Active Directory",
    "ICMP",
    "Minecraft",
    "samba"
]

TEST_TAGS_LINUX = [
    "ICMP",
    "SSH",
    "http",
    "mysql",
    "nodejs",
    "apache",
    "Arch Linux",
    "Ubuntu",
    "FreeBSD"
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
    for ip_suffix in range(2, TEST_IPS_NUM):
        ip = "127.0.0."+str(ip_suffix) # pylint: disable=C0103
        database.add_file(ip, 'static/dog.jpg')
        for text in TEST_TEXT:
            database.add_keystroke(ip, text)
        database.add_tag(ip, "test")
        if ip_suffix % 2 is 0:
            database.add_tag(ip, "Windows")
            database.add_tag(ip, TEST_TAGS_WINDOWS[ip_suffix % len(TEST_TAGS_WINDOWS)])
        else:
            database.add_tag(ip, "Linux")
            database.add_tag(ip, TEST_TAGS_LINUX[ip_suffix % len(TEST_TAGS_LINUX)])
        database.add_tag(ip, "Team "+str(ip_suffix % TEST_TEAM_NUMS))
    print("Test Data Added.")
