#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INFORMATION RETRIEVAL IN INDIAN LANGUAGE(HINDI)
@author: narayanashanmukhavenkat
"""
import numpy as np
from nltk.corpus import indian, stopwords
from gensim import corpora, models, similarities, matutils
from gensim.models import lsimodel, nmf

documents = indian.sents("hindi.pos")

temp = open("hindisw.txt", 'r')

stop_words = ""
stop_words = stop_words + temp.read()
temp.close()

stop_words = [word for word in stop_words.split()]

texts = [[word for word in document if word not in stop_words] for document in documents]

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/tmp/ir.mm', corpus)

lsi = models.LsiModel(corpus,  num_topics=43, id2word = dictionary)

index = similarities.MatrixSimilarity(lsi[corpus])

doc = "अनवर विंसेट रन आउट"

vec_bow = dictionary.doc2bow(doc.split())

vec_lsi1 = lsi[vec_bow]

sims = index[vec_lsi1]

sims = sorted(enumerate(sims), key=lambda item: -item[1])

print(sims)

print('#####################################################')

nmfmodel = nmf.Nmf(corpus, num_topics=43, id2word = dictionary, normalize =True)
 
index = similarities.MatrixSimilarity(nmfmodel[corpus])

vec_lsi2 = nmfmodel[vec_bow]        

sims = index[vec_lsi2]

sims = sorted(enumerate(sims), key=lambda item: -item[1])

print(sims)











