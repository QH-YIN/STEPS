import sys
import time
import json
import logging
import requests
ip = requests.get("http://169.254.169.254/latest/meta-data/public-ipv4").content
from multiprocessing import Process

def run_requests(proc_no, http_req):
      print("run_requests")
      rsp = requests.post(http_req,data={'E-Mail Address':1,'Password':1})

      if rsp.status_code >=400:
         print("Request failed", rsp.text)


######################################################################################
#                      Run the load-tests on the endpoint                            #
######################################################################################
if __name__=="__main__":
   #Configure port on which your application is reachable
   port = "3000"

   #Configure the number of requests you want to execute on your endpoint
   no_of_requests = "1000"

   #Job_name can be your load test id/name which will help you identify the load test uniquely
   job_name = "Test-case-1.2"

   #Job_log which can act as a repository later to identify more about the test-cases executed duri$
   log_file = "Test-case-1.2.log"
   #test_hostname would your application hosted
   test_hostname = "localhost"

   #Initialize the loggin module in python
   logging.basicConfig(filename=log_file,
                                filemode='w',
                                format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                                datefmt='%H:%M:%S',
                                level=logging.DEBUG)
   logger = logging.getLogger()

   #Inform dynatrace the next set of requests are part of this load-test
   #eventdetail = "STARTING LOADTEST"
   #push_event(logger, eventdetail, job_name)
   #Generate the load
   load_test(port, no_of_requests, logger, test_hostname)

   #Inform dynatrace about completion of load-test
   #eventdetail = "STOPPING LOADTEST"
   #push_event(logger, eventdetail, job_name)

   logging.shutdown()

