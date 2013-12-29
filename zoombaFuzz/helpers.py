#!/usr/bin/env python
"""
zoombaFuzz - A Brainless Brute force Fuzzer
usage: PROGRAM [options] <...>
	-v	Verbose logging
	-l log_file Log output to logfile
Copyright (C) 2013 Achin K, mail: achin.kulshrestha@citrix.com
"""
import urllib
import urllib2
import datetime

def make_request(Address, HTTPMethod="GET", HTTPData=None, HTTPHeaders=None):
    
    if type(HTTPHeaders) != dict and HTTPHeaders != None:
        raise TypeError, ("Something Wrong with the Header Format")
    if type(HTTPData) != str and HTTPData != None:
        raise TypeError, ("Something wrong with the HTTPData Format")
    
    if HTTPHeaders:
        req = urllib2.Request(Address, HTTPMethod, HTTPHeaders=HTTPHeaders)
        
    else:
        req = urllib2.Request(Address, HTTPMethod)
        
    req.get_method = lambda: HTTPMethod.upper()  
    req.add_data(HTTPData)
    
    
    # Lot of Things can go wrong here, playing safe
    try:
        timeBegin = datetime.datetime.now()
        HTTPResponse = urllib2.urlopen(req)
        
        timeEnd = datetime.datetime.now()
    except urllib2.HTTPError, error:
        return(error.HTTPHeaders, error.msg, error.code, None)
    except urllib2.URLError, error:
        
        return(None, error.reason, None, None)
    else:
        HTTPHeaders = HTTPResponse.info()        
        responseContent = HTTPResponse.read()
        
        
        code = HTTPResponse.getcode()
        
        time = timeEnd - timeBegin
        return(HTTPHeaders, responseContent,code, time)
    
