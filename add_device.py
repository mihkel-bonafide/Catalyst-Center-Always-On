#!/usr/bin/env python3

"""
Author: MPG
Purpose: This is/was designed to add a new device to the Catalyst Center environment, except it appears Cisco's Always On
sandbox has removed POST permissions for regular folks like moi. Will need to test in the future in a reserved room.  -9/22/25 MPG

"""
import requests
from authenticate import get_token
from lehost import url
import urllib3
urllib3.disable_warnings()
import json

def add_device(): 
    # get your token and headers in order, my friend
    token = get_token()
    leheaders = {
            "Content-Type": "application/json",
            "X-Auth-Token": token
        }
    lebody = '''{ "type": "Cisco Catalyst Mihkthousand", "managementIpAddress": "1.2.3.4" }'''

    # this is your POST request 
    response = requests.post(url, headers=leheaders, data=lebody, verify=False)
    if response.ok:
        print(response.json())
    else:
        print(f"post request failed with code {response.status_code}")
        print(f"Failure body: {response.text}")


def main():
    add_device()   


if __name__ == "__main__":
    main()      