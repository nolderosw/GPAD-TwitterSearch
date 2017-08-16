#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pymongo import MongoClient
import datetime
import pprint


cliente = MongoClient('localhost', 27017)
banco = cliente.twitters
twitters_BD = banco.twitters_campina

#cliente = MongoClient('mongodb://localhost:27017/') essa tb funciona!!!

#banco = cliente.test_database

#banco = cliente['test-database'] tb funciona!!

#album = banco.test_collection #selecao de uma collection

#album = banco['test-collection'] forma alternativa
def convertmonth2ptbr(month):
    if(month == 'Jan'):
        return 'Janeiro'
    elif(month == 'Feb'):
        return 'Fevereiro'
    elif(month == 'Mar'):
        return 'Março'
    elif(month == 'Apr'):
        return 'Abril'
    elif(month == 'May'):
        return 'Maio'
    elif(month == 'June'):
        return 'Junho'
    elif(month == 'July'):
        return 'Julho'
    elif(month == 'Aug'):
        return 'Agosto'
    elif(month == 'Sept'):
        return 'Setembro'
    elif(month == 'Oct'):
        return 'Outubro'
    elif(month == 'Nov'):
        return 'Novembro'
    elif(month == 'Dec'):
        return 'Dezembro'
'''musicas = [
                  {
                    "_id": 1,
                    "nome": "Radioactive",
                    "banda": "Imagine Dragons",
                    "categorias": ["indie", "rock"],
                    "lancamento": datetime.datetime.now()
                  },
                  {
                    "_id": 2,
                    "nome": "Hear Me",
                    "banda": "Imagine Dragons",
                    "categorias": ["indie", "rock"],
                    "lancamento": datetime.datetime.now()
                  },
                  {
                    "_id": 3,
                    "nome": "Demons",
                    "banda": "Imagine Dragons",
                    "categorias": ["indie", "rock"],
                    "lancamento": datetime.datetime.now()
                  },
                  {
                    "_id": 4,
                    "nome": "Nothing Left To Say",
                    "banda": "Imagine Dragons",
                    "categorias": ["indie", "rock"],
                    "lancamento": datetime.datetime.now()
                  },
                  {
                    "_id": 5,
                    "nome": "Amsterdam",
                    "banda": "Imagine Dragons",
                    "categorias": ["indie", "rock"],
                    "lancamento": datetime.datetime.now()
                  }
              ] #definição de um array de json teste qualquer!!'''

#album = banco.album #criei um novo bd de albuns

'''musica = {
              "_id": 6,
              "nome": "teste",
              "banda": "TESTE BANDA",
              "categorias": ["indie", "rock"],
              "lancamento": datetime.datetime.now()
             }'''
#musica_id = album.insert_one(musica)
#album.insert_many(musicas) #inserindo no BD o array de json
#print (album.find_one())
#print (album.find_one({"nome": "Radioactive"}))
#print (album.find_one({"_id": 1}))
#album.delete_one({})
#for musica_id in range(album.count()):
 #       print (album.find_one({"_id": musica_id+1}))
#c = 0
#for i in range(twitters_BD.count()):
#    print(twitters_BD.find()[i]['id'])
#    c += 1
#print (c)
#print(twitters_BD.find()[0]['user']['screen_name'])
#print(twitters_BD.find()[0]['text'])
for i in range(twitters_BD.count()):
    print('Usuário:',twitters_BD.find()[i]['user']['screen_name'])
    print('Tweet:',twitters_BD.find()[i]['text'])
    createdAt = twitters_BD.find()[i]['created_at'].split()
    mes = convertmonth2ptbr(createdAt[1])
    dia = createdAt[2]
    ano = createdAt[5]
    hora = createdAt[3].split(':')
    print('Data:', dia,'de', mes, 'de',ano)
    print('Hora:', abs(int(hora[0])-3),'h',hora[1],'m',hora[2],'s')
    print('Localização:',twitters_BD.find()[i]['user']['location'],'\n\n')

#print(twitters_BD.find({'id':846369283303247872}).count())
#pprint.pprint(twitters_BD.find()[twitters_BD.count()-1])





