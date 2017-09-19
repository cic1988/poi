#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# Demo easy usage of REST
#

import json

from DatabaseAPI3 import *

api = DatabaseAPI("http://nv-panda:8080/iv.yuan", "admin", "yuan")

api.login()

with open('exported-pois.json', "r") as inputfile:
    pois_in = json.loads(inputfile.read())
    api.update('api/pois', None, pois_in)
    #print(inputfile.read())
