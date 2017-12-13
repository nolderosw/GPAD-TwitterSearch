import sys
from TwitterSearch import *
import datetime, dateutil.parser

reload(sys)
sys.setdefaultencoding('utf-8')

lat = float(sys.argv[1])
lng = float(sys.argv[2])
raio = int(sys.argv[3])/1000

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['febre amarela']) # let's define all words we would like to have a look for
    tso.set_geocode(lat,lng,raio,imperial_metric=False)

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'Xh7baOkXWZmWuTaaC8Ttvb6gt',
        consumer_secret = 'MRGwcVcXGYzFRWfo8Sr3F5lrFLSk6x5hCEZV4wg59WXcOFlgnU',
        access_token = '42270820-0CkVGeEKKD2uTyifkPJKch6T4kTHOCZ9WgwFu2bWN',
        access_token_secret = 'JGbTroE9hOfnIgPwOVBqrHbztUSaX2nbrH09WA2Egl8Pj'
     )

     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        data_timezone = ""
        tweet['created_at'] = tweet['created_at'].split(' ')
        temp_hora = int(tweet['created_at'][3].split(':')[0]) - 3
        tweet['created_at'][3] = str(temp_hora)+":"+tweet['created_at'][3].split(':')[1]+":"+tweet['created_at'][3].split(':')[1]
        for i in range(len(tweet['created_at'])):
            data_timezone = data_timezone+tweet['created_at'][i] + ' '
        
        data = dateutil.parser.parse(data_timezone) #converte a data para ficar bonitinha
        print('@%s tweetou: %s em %s' % (tweet['user']['screen_name'], tweet['text'], data.strftime('%m/%d/%Y %H:%M:%S')))

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)