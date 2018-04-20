"""
Integration with pwnboard.win
Author: Chris Vantine
Author: Micah Martin
"""
import requests
import json


def sendUpdate(ips, name="oceanview"):
    host = "https://pwnboard.win/generic"
    data = {'ips': ips, 'type': name}
    try:
        req = requests.post(host, json=data, timeout=3)
        print(req.text)
        return True
    except Exception as E:
        print(E)
        return False