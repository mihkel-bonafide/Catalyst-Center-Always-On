#!/usr/bin/env python3

"""
Author: MPG
Purpose: This is working code for the developer sandbox at developer.cisco.com. Specifically, this hits the 
'v1/network-device' endpoint to retrieve a list of network devices managed by Cisco Catalyst Center, and 
writes the output to a file named 'output.json'. HTTP status code is printed to the terminal. -9/17/25 MPG

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
    print(response.status_code)  
    with open('output.json', 'w') as f:
        json.dump(response.json(), f, indent=4) # if output.json already exists in your working dir, this will overwrite it


def main():
    get_devices()   


if __name__ == "__main__":
    main()  