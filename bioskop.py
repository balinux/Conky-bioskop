#!/usr/bin/env python

import requests
import urllib2
import json

url 	=  'http://ibacor.com/api/jadwal-bioskop?id=9'

nonton 	= requests.get(url)
nontonjson = nonton.json()

for item in nontonjson['data']:

	print ">>",item['movie'],"<<||>>", item['genre'],"\n"
