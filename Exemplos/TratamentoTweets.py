from pymongo import MongoClient
import re
import nltk
import string
import unicodedata

# Criação da conexão com banco de dados e de um cursor para pecorrer
cliente = MongoClient('localhost', 27017)
banco = cliente.twitters_febre_dor
twitters_BD = banco.matogrosso_do_sul
cursor = twitters_BD.find()

def criar_tokens(lista_tweets):
    """Faz a tokenização dos tweets"""

    tokens = [nltk.word_tokenize(tweet) for tweet in lista_tweets]

    return tokens


def retirar_stopwords(lista_tweets):
    """Retira os stopwords e pontuações da frase"""

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
    """Retira os stopwords e pontuações da frase"""

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
    """Remove hashtags dentro dos tweets"""

    novos_tweets = []

    for tweet in lista_tweets:
        texto = re.sub(r"#\S+", "", tweet)
        novos_tweets.append(texto)

    return novos_tweets


def remove_usuario(lista_tweets):
    """Remove hashtags dentro dos tweets"""

    novos_tweets = []

    for tweet in lista_tweets:
        texto = re.sub(r"@\S+", "", tweet)
        novos_tweets.append(texto)

    return novos_tweets


def remove_urls(lista_tweets):
    """Remove as urls dos tweets"""

    novos_tweets = []

    for tweet in lista_tweets:
        texto = re.sub(r"http\S+", "", tweet["text"])
        novos_tweets.append(texto)

    return novos_tweets


def imprimi_tweets(lista):
    """Imprimi lista de tweets"""

    for texto in lista:
        print(texto)


tweets = remove_urls(cursor)
tweets = remove_hashtag(tweets)
tweets = remove_usuario(tweets)
tweets = criar_tokens(tweets)
tweets = retirar_stopwords(tweets)
tweets = retirar_acentos(tweets)
imprimi_tweets(tweets)
