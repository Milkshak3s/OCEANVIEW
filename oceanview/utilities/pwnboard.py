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
    print("ips: " + ips)
    print("Data" + data)
    try:
        req = requests.post(host, json=data, timeout=3)
        print(req.text)
        return True
    except Exception as E:
        print("pwnboard Exception: " + E)
        return False