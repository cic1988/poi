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

response = api.get('api/pois')

for poi in response:
    api.remove('api/pois/%s' % (poi['id']))
