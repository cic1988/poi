#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Demo easy usage of REST
#

import json
import os.path

from DatabaseAPI3 import *

def doPOIImport(poi):
    # need to first form the single POI as a list
    poiImport = []
    poiImport.append(poi)

    response = api.insert('api/pois', poiImport)

    if not response:
        print("import POI failed...")
    else:
        print("import POI - %s" % (response[0]['id']))

api = DatabaseAPI("http://192.168.1.8:8080/iv.yuan", "admin", "yuan")

api.login()

# get the import file as input
filename = input("enter the import file name: ")

# check if file exists
if os.path.exists(filename) == True:
    with open(filename, "r") as inputfile:
        pois = json.loads(inputfile.read())

        #try to import the pois individually
        for poi in pois:
            # check whether the POI with the given id is there?
            poiID = poi['id']

            if poiID != None:
                print("POI ID can only be null - import ignored")
            else:
                doPOIImport(poi)
else:
    print("... file does not exist, give up import")
