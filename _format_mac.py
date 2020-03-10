#!/usr/bin/env python
# see https://stackoverflow.com/questions/11006702/elegant-format-for-a-mac-address-in-python-3-2
import re

def format_mac(mac: str) -> str:
    mac = mac.strip() # remove any whitespace
    mac = re.sub('[.:-]', '', mac).lower()  # remove delimiters and convert to lower case
    mac = ''.join(mac.split())  # remove whitespaces
    try: 
        assert len(mac) == 12  # length should be now exactly 12 (eg. 008041aefd7e)
    except:
        print(mac+" is not a valid MAC Address")
    assert mac.isalnum()  # should only contain letters and numbers
    # convert mac in canonical form (eg. 00:80:41:ae:fd:7e)
    mac = ":".join(["%s" % (mac[i:i+2]) for i in range(0, 12, 2)])
    return mac
