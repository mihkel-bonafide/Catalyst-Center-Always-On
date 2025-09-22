#!/usr/bin/env python3

"""
Author: MPG
Purpose: This is simply a different version of the get_device_info module, with arguably
cleaner syntax.  -9/22/25 MPG

"""
import requests
from authenticate import get_token
from lehost import url
import urllib3
urllib3.disable_warnings()
import json

def get_devices(): 
    # get your token and headers in order, my friend
    token = get_token()
    leheaders = {
            "Content-Type": "application/json",
            "X-Auth-Token": token
        }
    # this is your GET request 
    response = requests.get(url, headers=leheaders, verify=False)
    if response.ok:
        for iterator in response.json()['response']:
            print(f"Device ID: {iterator['id']}  Management IP: {iterator['managementIpAddress']}")
    else:
        print(f"Device collection failed with code {response.status_code}")
        print(f"Failure body: {response.text}")


def main():
    get_devices()   


if __name__ == "__main__":
    main()      