#!/usr/bin/evn python
import http.client
import ssl
import json
from _jamf_headers import headers
from _format_mac import format_mac
def jamf_api_query():
    no_verify = ssl._create_unverified_context()
    JAMF_PRO = 'itscasdb01.thecrick.org:8443'
    conn = http.client.HTTPSConnection(JAMF_PRO,context=no_verify)
    ## printf "username:password" | iconv -t ISO-8859-1 | base64 -i -
    #https://developer.jamf.com/sample-code
    # Create a local file called _jamf_headers.py containing this:
    #headers = {
    #    'authorization': "Basic YOUR_CREDENTIALS",
    #    'Accept': 'application/json',
    #}
    conn.request("GET","/JSSResource/computers/subset/basic",headers=headers)
    res = conn.getresponse()
    data = res.read()
    output_d = {}
    computers = json.loads(data.decode("utf-8"))
    # produce a dict, key is mac_address, value is list [username, serial_number]
    for computer in computers['computers']:
        mac_address = format_mac(computer['mac_address'])
        username = computer['username']
        serial_number = computer['serial_number']
        my_list = [username, serial_number]
        output_d[mac_address] = my_list
    return output_d
