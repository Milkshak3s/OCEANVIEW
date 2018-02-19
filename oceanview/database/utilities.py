"""
Various functions that are required by other modules
Author: Micah Martin
"""

# pylint: disable=W0702
def validate_ip(addr):
    """
    Validate that an IP address is legitimate
    """
    try:
        vals = [(int(i) < 256) for i in addr.split(".")]
        vals += [len(vals) == 4]
        return all(vals)
    except:
        return False
