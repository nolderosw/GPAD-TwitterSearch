#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import TwitterSearch
from pymongo import MongoClient
cliente = MongoClient('localhost', 27017)
banco = cliente.twitters
#twitters_BD = banco.twitters_bd
twitters_BD = banco.twitters_campina
try:
    tso = TwitterSearch.TwitterSearchOrder() # create a TwitterSearchOrder object 
    #tso.set_keywords(['dengue','dor'])# let's define all words we would like to have a look for
    #tso.set_keywords(['perda de apetite'])
    #tso.set_keywords(['Ictericia'])
    #tso.set_keywords(['dor','febre'])
    tso.set_keywords([' '])
    tso.set_geocode(-7.227165,-35.894873,30,imperial_metric=False) #campina
    #tso.set_geocode(-18.555948, -44.476655,250) #minas gerais
    #tso.set_keywords(['febre amarela'])
    #tso.set_language('pt') # we want to see pt tweets only
    #tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    '''
    ts = TwitterSearch.TwitterSearch(
        consumer_key = 'Xh7baOkXWZmWuTaaC8Ttvb6gt',
        consumer_secret = 'MRGwcVcXGYzFRWfo8Sr3F5lrFLSk6x5hCEZV4wg59WXcOFlgnU',
        access_token = '42270820-0CkVGeEKKD2uTyifkPJKch6T4kTHOCZ9WgwFu2bWN',
        access_token_secret = 'JGbTroE9hOfnIgPwOVBqrHbztUSaX2nbrH09WA2Egl8Pj'
     )
    '''
    ts = TwitterSearch.TwitterSearch(
        consumer_key = 'mfJfp2Vp8RvcSiIQ78QBGAbIu',
        consumer_secret = 'jXPlFJeDam7gapTxUTL17hfKK5NBflRnxM7yVuGL0hykObeTzg',
        access_token = '412444744-t0WvxJQiudwe8xzyqqEW009Mfw03W8YLXmnH1WoZ',
        access_token_secret = 'e0gbeKTtG1nFwvVrkc2lIyAO3lFopErIBc7cDweKvOP9H'
     )
    
    cont = 0
    twitters = []
     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        if(twitters_BD.find({'id':tweet['id']}).count() == 0 and tweet['text'].split()[0] != 'RT'):
            twitters.append(tweet)
        #print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
        cont += 1
    if(len(twitters) != 0):
        twitters_BD.insert_many(twitters)
    print ('Quantidade de tweets encontrados:',cont)
    print ('Quantidade de tweets novos no BD:',len(twitters))

except TwitterSearch.TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
