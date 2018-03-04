"""
Various functions that are required by other modules
Author: Micah Martin
"""

TEST_IPS_NUM = 254
TEST_TEAM_NUMS = 11

TEST_TEXT = [
    b"<5p3c1@l> Chars work &<|>",
    b"This text data was inserted by passing OCEANVIEW the 'maketestdb' command.",
    b"This is a Test IP."
]

TEST_TAGS_WINDOWS = [
    "ICMP",
    "http/nodejs",

    "VoIP",
    "Samba",
    "FTP",

    "Minecraft",
    "Steam",
    "Printer?",
    "418 TEAPOT",
    "rdp",
    "Active Directory",
    "NTP"
]

TEST_TAGS_LINUX = [
    "ICMP",
    "http/nginx",

    "mysql",
    "php",
    "Samba",
    "FTP",

    "SSH",
    "Arch",
    "Ubuntu",
    "CentOS",
    "FreeBSD",
    "Gentoo"
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
    # Variable database of tuples
    files = []
    keys = []
    tags = []
    ips = []
    print("Generating test data... ", end=' ', flush=True)
    for ip_suffix in range(2, TEST_IPS_NUM):
        ip = "127.0.0."+str(ip_suffix) # pylint: disable=C0103
        ips.append((ip,))
        files.append((ip, '/static/dog.jpg'))
        for text in TEST_TEXT:
            keys.append((ip, text))
        tags.append((ip, "test"))
        if ip_suffix % 2 is 0:
            tags.append((ip, "Windows"))
            tags.append((ip, TEST_TAGS_WINDOWS[round(ip_suffix/2) % len(TEST_TAGS_WINDOWS)]))
        else:
            tags.append((ip, "Linux"))
            tags.append((ip, TEST_TAGS_LINUX[round((ip_suffix+1)/2) % len(TEST_TAGS_LINUX)]))
        tags.append((ip, "Team "+str(ip_suffix % TEST_TEAM_NUMS)))
    print("Done!")
    print("Adding IPS... ", end=' ', flush=True)
    database.add_bulk_ips(ips)
    print("Done!")
    print("Adding Files... ", end=' ', flush=True)
    database.add_bulk_files(files)
    print("Done!")
    print("Adding Keystrokes... ", end=' ', flush=True)
    database.add_bulk_keystrokes(keys)
    print("Done!")
    print("Adding Tags... ", end=' ', flush=True)
    database.add_bulk_tags(tags)
    print("Done!")
    print("Test Data Added.")
