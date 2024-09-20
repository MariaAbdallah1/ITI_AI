import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
# Load the text  dataset
data = {
    "Text": ["the Hello, World!", 
             "This is an example", 
             "NLP is interesting interestted lovely",
             '<p>This is <b>HTML</b> content.</p>',
             'I love Python! 😃❤🚀',
             'Visit our website at https://www.example.com or email us at contact@example.com',
             'Ths is a wrd wth spellng mstaks']
}


df = pd.DataFrame(data)
def lowecaseTransformation():
    print (df["Text"].str.lower())

def removeSpecialCharacters():
    print( df["Text"].apply(lambda x: re.sub(r'[^\w\s]', '', x)))
# removeSpecialCharacters()
def Tokenize():
    print ( df["Text"].apply(lambda x: x.split()))

def Removestopwords():
    stop_words = set(stopwords.words("english"))
    print(' '.join([word for sentence in df['Text'] for word in sentence.split() if word not in stop_words]))

def Stemming():
    stemmer = PorterStemmer()
    print( ' '.join([stemmer.stem (word) for word in df['Text'][2].split()]))

from bs4 import BeautifulSoup
def RemoveHTML():
    print( BeautifulSoup(df['Text'][3], "html.parser").get_text())

import emoji
def RemoveEmoji():
    print (emoji.demojize(df['Text'][4]))
    print (re.sub(r'[^\x00-\x7F]+', '', df['Text'][4]))

def RemoveURLSandEmails():
    print (re.sub(r'http\S+|www\S+|[\w\.-]+@[\w\.-]+', '', df['Text'][5]))

from spellchecker import SpellChecker #install pyspellchecker
def Checkspelling():
    spell = SpellChecker()
    print (" ".join([spell.correction(word) for word in df['Text'][6].split()]))

# Checkspelling()