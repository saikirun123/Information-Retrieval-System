#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 19:27:58 2019

@author: narayanashanmukhavenkat
"""
import re,nltk
from nltk.corpus import stopwords
from pprint import pprint
from nltk.stem.porter import *
from gensim import corpora,models,similarities
documents = []
for counter in range(1033):
    temp = open(str(counter+1)+".txt", 'r')
    documents.append(temp.read())
    temp.close()    
stop_words = stopwords.words('english')   
texts = [[word for word in document.lower().split() if word not in stop_words] for document in documents]
dictionary = corpora.Dictionary(texts)
dictionary.save('/tmp/ir.dict')
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/tmp/ir.mm', corpus)
lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=400)
index = similarities.MatrixSimilarity(lsi[corpus])
index.save('/tmp/ir.index')
index = similarities.MatrixSimilarity.load('/tmp/ir.index')
doc = "medicosocial studies of hemophilia"
vec_bow = dictionary.doc2bow(doc.lower().split())
vec_lsi = lsi[vec_bow]
sims = index[vec_lsi] 
sims = sorted(enumerate(sims), key=lambda item: -item[1])
print(sims)
