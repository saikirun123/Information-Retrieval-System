"""
    Author: Narayana Shanmukha Venkat
"""
#installing dependencies
import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *

dir_input = input("Name of directory ::")
files = os.listdir(dir_input)
print('Files to be processed:-')
for file in files:
    print(file)
#The words to be removed will typically include words that often do not confer much semantic value
#Additionally, NLTK allows one to add his/her custom stop words

#Get a list of default English NLTK stop words
stop_words = stopwords.words('english')

#Adding custom words in the string given below
custom_stopwords = """all the words here are custom"""

#Adding custom words to the default English NLTK stop words list
stop_words += custom_stopwords.split()

for document in files:
    #File handling in python: Open a file and read it to the memory
    file = open(dir_input+"/"+document, 'r+')
    text = file.read()

    #Removing stopwords to clean the file
    doc = [word for word in text.split()]
    for stopper in stop_words:
        if stopper in doc:
            doc.remove(stopper)
    clean = list()

    for word in doc:
            if word.isalnum():
                clean.append(word.lower())
            else:
                #appending unicode character(s) that are not alphanumeric
                clean.append(u''.join(word.lower()))

    #Stemming is the process of reducing words to their word stem.
    #Stemmers remove morphological affixes from words, leaving only the word stem.

    #create a new Porter stemmer
    stemmer = PorterStemmer()

    #Applying stemming to clean the file
    clean = [stemmer.stem(word) for word in clean]

    #Creating Inverted Index Form for the given cleaned document
    inverted = {}
    for index, word in enumerate(clean):
            positions = inverted.setdefault(word, [])
            positions.append(index)
    file.truncate(0)
    file.write(str(inverted))
    print("\n"+"succesfully cleaned "+" "+file.name+"\n")
    file.close()
