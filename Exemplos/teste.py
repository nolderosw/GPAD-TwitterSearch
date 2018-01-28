import sys
from TwitterSearch import *
import datetime, dateutil.parser
import re
import nltk
import string
import unicodedata

reload(sys)
sys.setdefaultencoding('utf-8')

lat = float(sys.argv[1])
lng = float(sys.argv[2])
raio = int(sys.argv[3]) / 1000


def criar_tokens(lista_tweets):
    tokens = [nltk.word_tokenize(tweet) for tweet in lista_tweets]

    return tokens


def retirar_stopwords(lista_tweets):
    stopwords = nltk.corpus.stopwords.words("portuguese")

    regex = re.compile('[%s]' % re.escape(string.punctuation))
    nova_lista = []

    for index in range(len(lista_tweets)):
        nova_lista.append([])
        for palavra in lista_tweets[index]:
            nova_palavra = regex.sub(u'', palavra)
            if not nova_palavra == u'' and nova_palavra not in stopwords and not palavra.isdigit() and palavra != "RT":
                nova_lista[index].append(nova_palavra)

    return nova_lista


def retirar_acentos(lista_tweets):
    texto_limpo = []
    for indice in range(len(lista_tweets)):
        texto_limpo.append([])
        for palavra in lista_tweets[indice]:
            nfkd = unicodedata.normalize('NFKD', palavra)
            palavra_sem_acento = u''.join([c for c in nfkd if not unicodedata.combining(c)])
            q = re.sub('[^a-zA-Z0-9 \\\]', ' ', palavra_sem_acento)

            texto_limpo[indice].append(q.lower().strip())

    return texto_limpo


def remove_hashtag(lista_tweets):
    novos_tweets = []

    for tweet in lista_tweets:
        texto = re.sub(r"#\S+", "", tweet)
        novos_tweets.append(texto)

    return novos_tweets


def remove_usuario(lista_tweets):
    novos_tweets = []

    for tweet in lista_tweets:
        texto = re.sub(r"@\S+", "", tweet)
        novos_tweets.append(texto)

    return novos_tweets


def remove_urls(lista_tweets):
    novos_tweets = []

    for tweet in lista_tweets:
        texto = re.sub(r"http\S+", "", tweet["text"])
        novos_tweets.append(texto)

    return novos_tweets


def remove_unicode(lista_tweets):
    nova_lista = []
    for indice, palavras in enumerate(lista_tweets):
        nova_lista.append([])
        for palavra in palavras:
            if palavra != '':
                nova_lista[indice].append(str(palavra))
    return nova_lista


def imprimi_tweets(lista):
    for texto in lista:
        print(texto)


lista_tweets = []
lista_display = []
lista_tweets_tratados = []

try:
    tso = TwitterSearchOrder()  # create a TwitterSearchOrder object
    tso.set_keywords(['dor', 'febre'])  # let's define all words we would like to have a look for
    tso.set_geocode(lat, lng, raio, imperial_metric=False)

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key='Xh7baOkXWZmWuTaaC8Ttvb6gt',
        consumer_secret='MRGwcVcXGYzFRWfo8Sr3F5lrFLSk6x5hCEZV4wg59WXcOFlgnU',
        access_token='42270820-0CkVGeEKKD2uTyifkPJKch6T4kTHOCZ9WgwFu2bWN',
        access_token_secret='JGbTroE9hOfnIgPwOVBqrHbztUSaX2nbrH09WA2Egl8Pj'
    )

    # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        data_timezone = ""
        tweet['created_at'] = tweet['created_at'].split(' ')
        temp_hora = int(tweet['created_at'][3].split(':')[0]) - 3
        tweet['created_at'][3] = str(temp_hora) + ":" + tweet['created_at'][3].split(':')[1] + ":" + \
                                 tweet['created_at'][3].split(':')[1]
        for i in range(len(tweet['created_at'])):
            data_timezone = data_timezone + tweet['created_at'][i] + ' '

        data = dateutil.parser.parse(data_timezone)  # converte a data para ficar bonitinha
        # print('@%s tweetou: %s em %s' % (tweet['user']['screen_name'], tweet['text'], data.strftime('%d/%m/%Y %H:%M:%S')))
        lista_tweets.append(tweet)

    lista_tweets_tratados = remove_urls(lista_tweets)
    lista_tweets_tratados = remove_hashtag(lista_tweets_tratados)
    lista_tweets_tratados = criar_tokens(lista_tweets_tratados)
    lista_tweets_tratados = retirar_stopwords(lista_tweets_tratados)
    lista_tweets_tratados = retirar_acentos(lista_tweets_tratados)
    lista_tweets_tratados = remove_unicode(lista_tweets_tratados)

    cont = 0
    for tweet in lista_tweets:
        print('@%s tweetou: %s em %s twitter tratado: %s' % (
        tweet['user']['screen_name'], tweet['text'], data.strftime('%d/%m/%Y %H:%M:%S'), lista_tweets_tratados[cont]))
        cont = cont + 1
except TwitterSearchException as e:  # take care of all those ugly errors if there are some
    print(e)
