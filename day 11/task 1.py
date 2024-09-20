import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.sentiment.vader import SentimentIntensityAnalyzer

df = pd.read_csv('d:/Maria_iti/day 11/spam_dataset.csv')

df_sample = df.sample(n=50, random_state=1)

data = df_sample['text'].tolist()

def bag_of_words():
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(data)
    feature_names = vectorizer.get_feature_names_out()
    return pd.DataFrame(matrix.toarray(), columns=[f'bow_{name}' for name in feature_names], index=df_sample.index)

def tfidf():
    vectorizer = TfidfVectorizer()
    matrix = vectorizer.fit_transform(data)
    feature_names = vectorizer.get_feature_names_out()
    return pd.DataFrame(matrix.toarray(), columns=[f'tfidf_{name}' for name in feature_names], index=df_sample.index)

def ngrams():
    vectorizer = CountVectorizer(ngram_range=(2, 2))
    matrix = vectorizer.fit_transform(data)
    feature_names = vectorizer.get_feature_names_out()
    return pd.DataFrame(matrix.toarray(), columns=[f'ngram_{name}' for name in feature_names], index=df_sample.index)

def char_level_features():
    vectorizer = CountVectorizer(analyzer='char')
    matrix = vectorizer.fit_transform(data)
    feature_names = vectorizer.get_feature_names_out()
    return pd.DataFrame(matrix.toarray(), columns=[f'char_{name}' for name in feature_names], index=df_sample.index)

def pos_tagging():
    def extract_pos_features(text):
        tokens = word_tokenize(text)
        pos_tags = pos_tag(tokens)
        return ' '.join([tag for word, tag in pos_tags])
    
    pos_features = [extract_pos_features(text) for text in data]
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(pos_features)
    feature_names = vectorizer.get_feature_names_out()
    return pd.DataFrame(matrix.toarray(), columns=[f'pos_{name}' for name in feature_names], index=df_sample.index)

def lexical_features():
    def extract_lexical_features(text):
        words = word_tokenize(text)
        common_words = ["free", "buy", "click", "now"]
        return ' '.join([word for word in words if word in common_words])
    
    lexical_features = [extract_lexical_features(text) for text in data]
    vectorizer = CountVectorizer()
    matrix = vectorizer.fit_transform(lexical_features)
    feature_names = vectorizer.get_feature_names_out()
    return pd.DataFrame(matrix.toarray(), columns=[f'lexical_{name}' for name in feature_names], index=df_sample.index)

def sentiment_analysis():
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = [sia.polarity_scores(text) for text in data]
    sentiment_features = pd.DataFrame(sentiment_scores)
    sentiment_features.columns = [f'sentiment_{col}' for col in sentiment_features.columns]
    sentiment_features.index = df_sample.index
    return sentiment_features

bow = bag_of_words()
tf_idf = tfidf()
n_grams = ngrams()
char = char_level_features()
pos = pos_tagging()
lexical = lexical_features()
sentiment = sentiment_analysis()

dfs = [df_sample[['text']]]

if bow is not None:
    dfs.append(bow)

if tf_idf is not None:
    dfs.append(tf_idf)

if n_grams is not None:
    dfs.append(n_grams)

if char is not None:
    dfs.append(char)

if pos is not None:
    dfs.append(pos)

if lexical is not None:
    dfs.append(lexical)

if sentiment is not None:
    dfs.append(sentiment)

features_df = pd.concat(dfs, axis=1)

features_df.to_excel('d:/Maria_iti/day 11/spam_emails_features.xlsx', index=False)

print("Features and samples have been saved to 'spam_emails_features.xlsx'")
