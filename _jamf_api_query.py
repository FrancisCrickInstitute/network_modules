#!/usr/bin/evn python
import http.client
import ssl
import json
from _jamf_headers import headers, JAMF_URL
from _format_mac import format_mac
## printf "username:password" | iconv -t ISO-8859-1 | base64 -i -
#https://developer.jamf.com/sample-code
# Create a local file called _jamf_headers.py containing this:
#headers = {
#    'authorization': "Basic YOUR_CREDENTIALS",
#    'Accept': 'application/json',
#}
#JAMF_URL = 'jamf.domain:port'
'''
Usage
In [1]: from _jamf_api_query import jamf_api_query, jamf_get_computers
In [2]: jamf = jamf_api_query("/JSSResource/computers/subset/basic")
In [3]: type(jamf)
Out[3]: bytes
'''
def jamf_api_query(API_URI):
    no_verify = ssl._create_unverified_context()
    conn = http.client.HTTPSConnection(JAMF_URL,context=no_verify)
    conn.request("GET",API_URI,headers=headers)
    res = conn.getresponse()
    data = res.read()
    return data

'''
In [4]: computers = jamf_get_computers(jamf)
In [5]: computers
Out[5]:
{'MAC_ADDR1': ['user1', 'SERIAL_1'],
 'MAC_ADDR2': ['user2', 'SERIAL_2'],
 ...
 'MAC_ADDRN': ['userN', 'SERIAL_N'],
...}
'''
def jamf_get_computers(jamf_data):
    output_d = {}
    computers = json.loads(jamf_data.decode("utf-8"))
    # produce a dict, key is mac_address, value is list [username, serial_number]
    for computer in computers['computers']:
        mac_address = format_mac(computer['mac_address'])
        username = computer['username']
        serial_number = computer['serial_number']
        my_list = [username, serial_number]
        output_d[mac_address] = my_list
    return output_d
