"""
Various functions that are required by other modules
Author: Micah Martin
"""


def validate_ip(ip):
    """
    Validate that an IP address is legitimate
    """
    try:
        vals = [ (int(i) < 256) for i in ip.split(".") ]
        vals += [len(vals) == 4]
        return all(vals)
    except:
        return False

