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
    jason = response.json()
    print(response.status_code)  
    management_ips = [device['managementIpAddress'] for device in jason['response']] 
    device_ids = [device['id'] for device in jason['response']]  

    with open('output.json', 'w') as output_file:
        # full output from the GET request
        json.dump(jason, output_file, indent=4) 

    with open('devices.json', 'w') as dev_file:
        # just the device IDs and management IPs
        devices = dict(zip(device_ids, management_ips))
        json.dump(devices, dev_file, indent=4)
        

def main():
    get_devices()   


if __name__ == "__main__":
    main()  