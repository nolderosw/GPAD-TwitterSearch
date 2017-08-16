#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import oauth2
import json

#Define my keys
consumer_key = 'mfJfp2Vp8RvcSiIQ78QBGAbIu'
consumer_secret = 'jXPlFJeDam7gapTxUTL17hfKK5NBflRnxM7yVuGL0hykObeTzg'
token_key = '412444744-t0WvxJQiudwe8xzyqqEW009Mfw03W8YLXmnH1WoZ'
token_secret = 'e0gbeKTtG1nFwvVrkc2lIyAO3lFopErIBc7cDweKvOP9H'

#Define REST auths with oauth2 lib
consumer = oauth2.Consumer(consumer_key, consumer_secret);
token = oauth2.Token(token_key, token_secret);
cliente = oauth2.Client(consumer, token);

#request from twitter by URL twitter: 'https://dev.twitter.com/rest/public/search'
request = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=&geocode=-22.912214,-43.230182,1km&lang=pt&result_type=recent');

#decodify cliente
decodify = request[1].decode();

#transform to JSON object
json = json.loads(decodify);

print (json);