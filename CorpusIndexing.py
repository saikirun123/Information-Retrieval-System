"""
    Author: Narayana Shanmukha Venkat
"""
#!/usr/bin/env python
#installing dependencies
import re,nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *

_WORD_MIN_LENGTH = 3
#The words to be removed will typically include words that often do not confer much semantic value
#Additionally, NLTK allows one to add his/her custom stop words
#Get a list of default English NLTK stop words
""" ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    """
stop_words = stopwords.words('english')

#Adding custom words in the string given below
custom_stopwords = """all the words here are custom"""

#Adding custom words to the default English NLTK stop words list
stop_words += custom_stopwords.split()

def word_split(text):
    word_list = []
    wcurrent = []
    windex = None

    for i, c in enumerate(text):
        if c.isalnum():
            wcurrent.append(c)
            windex = i
        elif wcurrent:
            word = u''.join(wcurrent)
            word_list.append((windex - len(word) + 1, word))
            wcurrent = []

    if wcurrent:
        word = u''.join(wcurrent)
        word_list.append((windex - len(word) + 1, word))

    return word_list

#Stemming is the process of reducing words to their word stem.
#Stemmers remove morphological affixes from words, leaving only the word stem.
#create a new Porter stemmer
stemmer = PorterStemmer()
def words_cleanup(words):
    cleaned_words = []
    for index, word in words:
        if len(word) < _WORD_MIN_LENGTH or word in stop_words:
            continue
        cleaned_words.append((index, stemmer.stem(word)))
    return cleaned_words

def words_normalize(words):
    normalized_words = []
    for index, word in words:
        wnormalized = word.lower()
        normalized_words.append((index, wnormalized))
    return normalized_words

def word_index(text):
    words = word_split(text)
    words = words_normalize(words)
    words = words_cleanup(words)
    return words

def inverted_index(text):
    """
    Create a WORD LEVEL DOCUMENT SPECIFIC Inverted-Index of the specified text document.
        {word:[locations]}
    """
    inverted = {}

    for index, word in word_index(text):
        locations = inverted.setdefault(word, [])
        locations.append(index)

    return inverted

def inverted_index_add(inverted, doc_id, doc_index):
    """
     create a WORD LEVEL DOCUMENT UNSPECIFIC Inverted-Index
        {word:{doc_id:[locations]}}
    """
    for word, locations in doc_index.items():
        indices = inverted.setdefault(word, {})
        indices[doc_id] = locations
    return inverted

if __name__ == '__main__':
    sample1 = """
Vallabhbhai Patel was a political and social leader of India who played a major role in the country's struggle for independence and subsequently guided its integration into a united, independent nation. He was called the "Iron Man of India", and was often addressed as "Sardar" which means "Chief" or "Leader" in many languages of India.
"""

    sample2 = """
Vallabhbhai Patel already had a successful practice as a lawyer when he was first inspired by the work and philosophy of Mahatma Gandhi. Patel subsequently organised the peasants of Kheda, Borsad, and Bardoli in Gujarat in a non-violent civil disobedience movement against oppressive policies imposed by the British Raj; in this role, he became one of the most influential leaders in Gujarat. He rose to the leadership of the Indian National Congress and was at the forefront of rebellions and political events, organising the party for elections in 1934 and 1937, and promoting the Quit India movement.
"""

    inverted = {}
    documents = {'doc1':sample1, 'doc2':sample2}
    for doc_id, text in documents.items():
        doc_index = inverted_index(text)
        inverted_index_add(inverted, doc_id, doc_index)

    for word, doc_locations in inverted.items():
        print( word, doc_locations)



