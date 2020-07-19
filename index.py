# Importing Libraries
# Data Analysis
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data Preprocessing and Feature Engineering
from textblob import TextBlob
import re
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

# Model Selection and Validation
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# Reading test and training data
train_tweets = pd.read_csv('twitter_train.csv')
test_tweets = pd.read_csv('twitter_test.csv')

# Data Analysis
sns.countplot(x='label', data=train_tweets)


def form_sentence(tweet):
    tweet_blob = TextBlob(tweet)
    return ' '.join(tweet_blob.words)


print(form_sentence(train_tweets['tweet'].iloc[10]))
print(train_tweets['tweet'].iloc[10])
