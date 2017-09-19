#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Demo easy usage of REST
#

import json
import os.path

from DatabaseAPI3 import *

# change the URL and login
api = DatabaseAPI("http://192.168.1.8:8080/iv.yuan", "admin", "yuan")

api.login()

# get the export file as input
filename = input("enter the export file name: ")

doExport = True

# check if file exists
if os.path.exists(filename) == True:
    doExport = input("%s exists, are you sure to overwrite it? y/N: " % (filename)) == "y"

if doExport == True:
    with open(filename, 'w') as outputfile:
        json.dump(api.get('api/pois'), outputfile)
        print("... finish export")
else:
    print("... give up overwritting %s" % (filename))
