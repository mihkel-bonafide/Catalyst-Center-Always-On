#!/usr/bin/env python3

"""
Author: Mihkel Gardner
Purpose: Use the Python requests library to obtain an API access-token from 
Cisco Catalyst Center. 
"""
import requests
import urllib3
urllib3.disable_warnings()

def get_token():
    """
    Obtains the access token needed for subsequent API calls for Cisco Catalyst Center.
    """
    # Declare local variables
    lepath = "https://sandboxdnac2.cisco.com/dna"  # this works with or without that "2" btw, but will generate a different token
    leauth = ("devnetuser", "Cisco123!")
    leheaders = {"Content-Type": "application/json"}    
    endpoint = "/system/api/v1/auth/token"

    # Issue HTTP POST request to specified endpoint
    response = requests.post(url=lepath + endpoint, auth=leauth, headers=leheaders, verify=False)

    # If successful, print token. Else, raise HTTPError with relevant info 
    response.raise_for_status()
    token = response.json()["Token"]
    return token 

def main():
    """
    Execute me!
    """
    token = get_token()
    print(f"Token: {token}")    


if __name__ == "__main__":
    main()  
