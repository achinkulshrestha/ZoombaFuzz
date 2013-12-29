#!/usr/bin/env python
"""
zoombaFuzz - A Brainless Brute force Fuzzer
usage: PROGRAM [options] <...>
	-v	Verbose logging
	-l log_file Log output to logfile
Copyright (C) 2013 Achin K, mail: achin.kulshrestha@citrix.com
"""
import os
import sys

MODPATH = os.filePath.dirname(os.path.abspath(__file__))

def consuming_file(fileLocation):    
    filePath = MODPATH + fileLocation
    fileHandle = open(filePath, "rb")
    vals = list()
    
    for itemValue in fileHandle.readlines():
        if itemValue.startswith("# "):
            pass
        else:
            vals.append(itemValue.rstrip())
        
    fileHandle.close()
    
    return(vals)

class attack_payloads:
    class all_attacks:
        # Till Now implemented only the all-attack section of FuzzDB, please add more attacks as needed
        fileLocation = "/data/attack-payloads/all-attacks/all-attacks-unix.txt"
        all_attacks_unix = consuming_file(fileLocation)
        
        fileLocation = "/data/attack-payloads/all-attacks/all-attacks-win.txt"
        all_attacks_win = consuming_file(fileLocation)
        
        fileLocation = "/data/attack-payloads/all-attacks/interesting-metacharacters.txt"
        interesting_metacharacters = consuming_file(fileLocation)
        
