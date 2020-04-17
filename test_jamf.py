from _jamf_api_query import jamf_api_query, jamf_get_computers
from pprint import pprint
data =(jamf_api_query("/JSSResource/computers/subset/basic"))
computers = jamf_get_computers(data)
pprint(computers)
