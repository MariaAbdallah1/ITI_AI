import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re

data = ["Get a free iPhone now!", "Your invoice is due.", "Click here to win $1000!",
        "Meeting scheduled for tomorrow.", "Great job, keep it up!", "Bad product, never buying again."]

def bag_of_words():
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(data)
    print(vectorizer.get_feature_names_out())
    print (matrix.toarray())
# bag_of_words() 
def tfidf():
# TF(word, document) = (Number of times the word appears in the document) / (Total number of words in the document)
# IDF(word) = log(Total number of documents / Number of documents containing the word)
    # It measures the importance of a word across the entire corpus by penalizing words that 
    # appear frequently in many documents. 
# TF-IDF(word, document) = TF(word, document) * IDF(word)
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(data)
    print(vectorizer.get_feature_names_out())
    print (matrix.toarray())

def ngrams():
    data = ["love coding.", "Coding is fun."]
    vectorizer = CountVectorizer(ngram_range=(2, 2))
    matrix = vectorizer.fit_transform(data)
    print(vectorizer.get_feature_names_out())
    print (matrix.toarray())

def char_level_features():
    vectorizer = CountVectorizer(analyzer='char')
    matrix = vectorizer.fit_transform(data)
    print(vectorizer.get_feature_names_out())
    print (matrix.toarray())

def pos_tagging(data):
    def extract_pos_features(text):
        tokens = word_tokenize(text)
        pos_tags = pos_tag(tokens)
        return ' '.join([tag for word, tag in pos_tags])
    
    pos_features = [extract_pos_features(text) for text in data]
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(pos_features)
    print(vectorizer.get_feature_names_out())
    print (matrix.toarray())

def lexical_features():
    def extract_lexical_features(text):
        words = word_tokenize(text)
        common_words = ["free", "buy", "click", "now"]
        return ' '.join([word for word in words if word in common_words])
    
    lexical_features = [extract_lexical_features(text) for text in data]
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(lexical_features)
    print(vectorizer.get_feature_names_out())
    print (matrix.toarray())
lexical_features()
# neg: The proportion of negative sentiment in the document.
# neu: The proportion of neutral sentiment in the document.
# pos: The proportion of positive sentiment in the document.
# compound: The overall sentiment score, where a positive score indicates positive sentiment and a negative score indicates negative sentiment.
def sentiment_analysis():
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = [sia.polarity_scores(text) for text in data]
    sentiment_features = pd.DataFrame(sentiment_scores)
    print (sentiment_features)
# sentiment_analysis()

# def topic_modeling(data):
#     def preprocess_text(text):
#         text = re.sub(r'[^\w\s]', '', text)  # Remove special characters
#         text = text.lower()  # Convert to lowercase
#         return text
    
#     preprocessed_data = [preprocess_text(text) for text in data]
#     vectorizer = CountVectorizer(stop_words=stopwords.words('english'))
#     X = vectorizer.fit_transform(preprocessed_data)
#     lda = LatentDirichletAllocation(n_components=2)
#     lda_matrix = lda.fit_transform(X)
#     return lda_matrix