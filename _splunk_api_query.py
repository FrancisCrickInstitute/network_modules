#!/usr/bin/env python
from _format_mac import format_mac
import sys 
from time import sleep
import splunklib.results as results
import splunklib.client as client
from _crick_splunk_creds import crick_splunk_d
# Create a file called _splunk_creds.py 
#    splunk_creds_d = {
#        'host':"hostname.domain",
#        'port':8089,
#        'username':'',
#        'password':'',
#    }
def splunk_api_query(SDOUT, query_string):
    service = client.connect(**crick_splunk_d)
    #searchquery_normal = "search * | head 10"
    searchquery_normal = query_string
    kwargs_normalsearch = {"exec_mode": "normal"}
    job = service.jobs.create(searchquery_normal, **kwargs_normalsearch)
    # A normal search returns the job's SID right away, so we need to poll for completion
    while True:
        while not job.is_ready():
            pass
        stats = {"isDone": job["isDone"],
                 "doneProgress": float(job["doneProgress"])*100,
                  "scanCount": int(job["scanCount"]),
                  "eventCount": int(job["eventCount"]),
                  "resultCount": int(job["resultCount"])}
        status = ("\r%(doneProgress)03.1f%%   %(scanCount)d scanned   "
                  "%(eventCount)d matched   %(resultCount)d results") % stats
        if SDOUT:
            sys.stdout.write(status)
            sys.stdout.flush()
        if stats["isDone"] == "1":
            if SDOUT:
                sys.stdout.write("\n\nDone!\n\n")
            break
        sleep(2)
    # Get the results and display them
    return results.ResultsReader(job.results())
