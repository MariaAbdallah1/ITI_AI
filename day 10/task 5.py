import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import nltk

nltk.download('stopwords')

df = pd.read_csv("d:/Maria_iti/day 10/spam_ham_dataset.csv")

df["text"] = df["text"].str.lower()
df["text"] = df["text"].apply(lambda x: re.sub(r'[^\w\s]', '', x))
df["text"] = df["text"].apply(lambda x: x.split())

stop_words = set(stopwords.words("english"))
df["text"] = df["text"].apply(lambda x: [word for word in x if word not in stop_words])

stemmer = PorterStemmer()
df["text"] = df["text"].apply(lambda x: [stemmer.stem(word) for word in x])

df["text"] = df["text"].apply(lambda x: re.sub(r'http\S+|www\S+|[\w\.-]+@[\w\.-]+', '', ' '.join(x)).split())

df["text"] = df["text"].apply(lambda x: ' '.join(x))

df.to_csv("d:/Maria_iti/day 10/cleaned_spam_ham_dataset.csv", index=False)