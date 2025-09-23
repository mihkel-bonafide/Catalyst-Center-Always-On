This is working code that connects to the Catalyst Center (formerly DNA Center) Always On developer 
sandbox (developer.cisco). It returns two files: 1. output.json lists the full output from the
"/dna/intent/api/v1/network-device", which is the full list of devices including 52 data fields.
The 2nd file, devices.json, extracts only the unique device ID and the management ID as JSON objects.