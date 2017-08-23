from pymongo import MongoClient
import tweepy
import json
from pprint import pprint
import pandas

consumer_key = 'eLHkDpZCcpOqBM3JipDTktNMA'
consumer_secret = 'Z0UND2lOgl5WdgzOV1UZf3Ogo6HAaNiWrBu6Tjl7FWz74x1saU'
access_token = '859897569908064256-b2myOYtVPuYOCVkEOrEQkgEm0FWKQPv'
access_token_secret = 'P0M3QEO86NP7Fg6ovzGCCbO0U1FwOvxZfIkU2wdAQ1ffi'

cliente = MongoClient('localhost', 27017)
banco = cliente.dados
twitters_BD = banco.Febre_Amarela

#col = db.tweets

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

keywords = ['dor','cabeca','vomito','vomitando','tontura']

class MyListener(tweepy.StreamListener):
    def on_data(self, dados):
        tweet = json.loads(dados)
        created_at = tweet["created_at"]
        name = tweet["user"]["name"]
        text = tweet["text"]
        if text[0] == 'R' and text[1] == 'T' and text[2] == ' ':
            rt = True
        else:
            rt = False

        obj = {"created_at" : created_at, "name" : name, "text" : text,}
        #tweetind = col.insert_one(obj).inserted_id
        print('Nome: %s\nMensagem: %s\nData de Criação: %s\nStatus de rt: %s\n' % (name, text, created_at, rt))
        #pprint(tweet)
        # TWEED ARMAZENADO
        twitters_BD.insert_one(tweet).inserted_id
        return True


    #def on_status(self, status):
    #    if 'febre amarela' in status.text.lower():
    #        print(status.text)

    def on_error(self, status_code):
        print("Error : %d" %status_code)
        return True

    def on_timeout(self):
        print("Timeout")
        return True

my_listener = MyListener()

my_stream = tweepy.Stream(auth, listener=my_listener)

my_stream.filter(track=keywords)