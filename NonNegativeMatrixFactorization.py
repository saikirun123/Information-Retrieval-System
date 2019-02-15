#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 19:27:58 2019

@author: narayanashanmukhavenkat
"""
import numpy as np
from nltk.corpus import stopwords
from gensim import corpora, models, similarities, matutils
from gensim.models import lsimodel, nmf
from gensim.models.coherencemodel import CoherenceModel 

documents = []

for counter in range(1033):
    temp = open(str(counter+1)+".txt", 'r')
    documents.append(temp.read())
    temp.close()

stop_words = stopwords.words('english')

texts = [[word for word in document.lower().split() if word not in stop_words] for document in documents]

dictionary = corpora.Dictionary(texts)
i=0
corpus = [dictionary.doc2bow(text) for text in texts]
#96351 total words
#20097 unique words
print(np.shape(np.array(corpus)))
#Convert document into the bag-of-words (BoW) format = list of (token_id, token_count) tuples.
corpora.MmCorpus.serialize('/tmp/ir.mm', corpus)

#lsi = models.LsiModel(corpus,  num_topics=43, id2word = dictionary)
#print(np.shape(np.array(lsi.projection.u))) # - left singular vectors
#print(np.shape(np.array(lsi.projection.s)))
#print(np.shape(np.array(matutils.corpus2dense(lsi[corpus], len(lsi.projection.s)).T / lsi.projection.s)))
#print(np.shape(np.array(lsi[corpus])))
#np.matmul(np.matmul(np.array(lsi.projection.u), np.array(lsi.projection.s)),np.array(matutils.corpus2dense(lsi[corpus], len(lsi.projection.s)).T / lsi.projection.s)) 
#index = similarities.MatrixSimilarity(lsi[corpus])
doc = "medicosocial studies of hemophilia"
vec_bow = dictionary.doc2bow(doc.lower().split())
f = open("output.txt", "a")
#for i in range(0, lsi.num_topics):
#    print(lsi.print_topic(i,10))
#vec_lsi1 = lsi[vec_bow]
#sims = index[vec_lsi1]
#sims = sorted(enumerate(sims), key=lambda item: -item[1])
#cm1 = CoherenceModel(model=lsi, corpus=corpus, coherence='u_mass')
#coherence = cm1.get_coherence()
#print('#####################################################')
#print(coherence)     

#print(sims)
nmfmodel = nmf.Nmf(corpus, num_topics=43, id2word = dictionary, normalize =True)
for i in range(0, 43):
    print(nmfmodel.print_topic(i,10))
    print('#########################')
print("DOCUMENT TOPICS OF MEDICOSOCIAL STUDIES OF HEMOPHILIA")
print(nmfmodel.get_document_topics(vec_bow))          
#print(nmfmodel._W)
#print(nmfmodel._h)
print(np.array(nmfmodel._W).shape)
print(np.array(nmfmodel._h).shape)
#print(nmfmodel._w_max_iter) #vec_lsi2 = lsi[vec_bow]
#sims = index[vec_lsi2]
#sims = sorted(enumerate(sims), key=lambda item: -item[1])
#cm2 = CoherenceModel(model=nmfmodel, corpus=corpus, coherence='u_mass')
#coherence = cm2.get_coherence()
#print('#####################################################')
#print(coherence)  
#print(sims)










