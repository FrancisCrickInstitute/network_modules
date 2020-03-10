#!/usr/bin/env python
import requests
from getpass import getpass
from pprint import pprint
SCCM_URL = "https://mercury-master.thecrick.org/AdminService/v2"

#session = requests.Session()
#user = 'admin-morrelg'
#password = getpass("Enter Admin SSO password: ")

#session.auth = (user, password)
response = requests.get(SCCM_URL)

print(response.status_code)

#pprint(response.json())
