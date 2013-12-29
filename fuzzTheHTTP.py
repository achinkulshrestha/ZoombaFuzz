#!/usr/bin/env python
"""
zoombaFuzz - A Brainless Brute force Fuzzer
usage: PROGRAM [options] <...>
	-v	Verbose logging
	-l log_file Log output to logfile
Copyright (C) 2013 Achin K, mail: achin.kulshrestha@citrix.com
"""
# import suds
import urllib2
import cgi
import sys, getopt, logging, re
import urllib
import logging
from urllib import urlencode
from itertools import product
from zoombaFuzz import helpers
from zoombaFuzz import fuzzdb

import os

def fuzz_the_param(tokenized_postdata, item):
    secondParam = tokenized_postdata.split('=')[1]
    secondParam = item
    firstParam = tokenized_postdata.split('=')[0]
    return firstParam+"="+secondParam


def fuzz_postdata(location,postdata,headers,fuzz_values):
    tokenized_postdata = postdata.split('&')
    for i in range(len(tokenized_postdata)):        
        for item in (fuzz_values):
            fuzzed_token = fuzz_the_param(tokenized_postdata[i],item)
            temp = tokenized_postdata
            temp[i]= fuzzed_token
            newpostdata = "&".join(temp)
            print newpostdata
            reheaders, content, code, time = utils.make_request(location, method="POST", postdata=newpostdata,headers=headers)
            logger.info("Reponse code %s and time taken %s ",code, time)

def fuzz_headers(location,postdata,headers,fuzz_values):
    for key in headers:
        logger.info("Fuzzing header %s ",key)
        for item in (fuzz_values):            
            headers[key] = item
            logger.info("Fuzzing with value %s ",item)
            resheaders, content, code, time = utils.make_request(location, method="POST", postdata=postdata,headers=headers)
            logger.info("Reponse code %s and time taken %s ",code, time)
            
       
def requestToFuzz():
    fuzz_post_values = fuzzdb.attack_payloads.all_attacks.all_attacks_win
    fuzz_header_values = fuzzdb.attack_payloads.all_attacks.all_attacks_win
    location = "boomboom.com"
    headers = {"Host": "boomboom.com",
               "User-Agent":"Mozilla/4.0 (compatible; MSIE 4.01; AOL 4.0; Mac_68K)",
              }
           
    postdata = "FooBar=Foodoodoodbar"
    
    fuzz_postdata(location,postdata,headers,fuzz_post_values)
    #fuzz_headers(location,postdata,headers,fuzz_header_values)
    


if __name__ == '__main__':

    __usage__ = __doc__.replace("PROGRAM", os.path.basename(sys.argv[0]))
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    fileHandler = None
    
    def die_usage(msg=""):
        sys.stderr.write("%s%s\n" % (__usage__, msg))
        sys.exit(1)

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hvl:", ["help", "verbose", "log-file"])
    except getopt.GetoptError, e:        
        die_usage(str(e))
    for o, a in opts:
        if o in ("-h","--help"): die_usage()
        if o in ("-v", "--verbose"): logger.setLevel(logging.DEBUG)                
        if o in ("-l", "--log-file"): fileHandler = logging.FileHandler("log.txt")
          
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    if (fileHandler is not None):
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)

    logger.info("ready (Ctrl+C to stop)")
    authorise()
    
    logger.info("stopped")
