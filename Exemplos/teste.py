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

sintomas_febre = ['cabeca','pele', 'amarela', 'olhos', 'olho', 'amarelos', 'amarelo', 'amarelado', 'amarelada', 'amarelados','nauseas', 'nausea','vomito', 'vomitar', 'vomitando']
sintomas_outas = ['musculos','articulacoes','articulares','articulacao','manchas', 'corpo', 'reacao']
estatisticas = []
estatisticas_gerais = []

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
            if not nova_palavra == u'' and nova_palavra not in stopwords and not bool(re.search(r'\d', palavra)) and palavra != "RT":
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

def get_estatisticas(lista_tweets):
    qt_baixa = 0
    qt_media = 0
    qt_alta = 0
    qt_geral = len(lista_tweets)
    for tweet in lista_tweets:
        score = 0
        for palavra in sintomas_febre:
            if (palavra in tweet):
                score = score + 1
        for palavra in sintomas_outas:
            if (palavra in tweet):
                score = score - 1
        if(score < 0):
            estatisticas.append('BAIXA')
            qt_baixa = qt_baixa + 1
        elif(score <= 1):
            estatisticas.append('MEDIA')
            qt_media = qt_media + 1
        elif(score > 1):
            estatisticas.append('ALTA')
            qt_alta = qt_alta + 1
    estatisticas_gerais.append(qt_baixa)
    estatisticas_gerais.append(qt_media)
    estatisticas_gerais.append(qt_alta)
    estatisticas_gerais.append(qt_geral)

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
        if(tweet['text'].split()[0] != 'RT'):
            lista_tweets.append(tweet)

    lista_tweets_tratados = remove_urls(lista_tweets)
    lista_tweets_tratados = remove_hashtag(lista_tweets_tratados)
    lista_tweets_tratados = remove_usuario(lista_tweets_tratados)
    lista_tweets_tratados = criar_tokens(lista_tweets_tratados)
    lista_tweets_tratados = retirar_stopwords(lista_tweets_tratados)
    lista_tweets_tratados = retirar_acentos(lista_tweets_tratados)
    lista_tweets_tratados = remove_unicode(lista_tweets_tratados)
    get_estatisticas(lista_tweets_tratados)

    cont = 0
    for tweet in lista_tweets:
        print('@%s tweetou: %s em %s com chance: %s' % (
        tweet['user']['screen_name'], tweet['text'], data.strftime('%d/%m/%Y %H:%M:%S'), estatisticas[cont]))
        cont = cont + 1
    print('Quantidade de twitters minerados: %d' % (len(lista_tweets_tratados)))
    print(estatisticas_gerais)
except TwitterSearchException as e:  # take care of all those ugly errors if there are some
    print(e)
