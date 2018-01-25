#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 20:27:06 2017

@author: wesley150
"""


from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

EXAMPLE_TEXT = "Olá senhor smith. Como você está hoje? Suponho que esteja bem, espero que esteja bem, está um dia lindo ali fora"

print(sent_tokenize(EXAMPLE_TEXT))

stop_words = set(stopwords.words('portuguese'))

print(stop_words)

	  
