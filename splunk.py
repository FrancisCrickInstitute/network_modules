from _splunk_api_query import splunk_api_query
from _crick_splunk_creds import crick_splunk_d 

foo = splunk_api_query(True, 'search eventtype=cisco-ise  MESSAGE_CLASS="Failed-Attempt"')
