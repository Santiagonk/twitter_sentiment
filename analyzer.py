import numpy as np

import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords

stopwords = set(stopwords.words('spanish'))

top_words = {}
tweets_topic = open('./paroNacional.txt', encoding='utf-8')
for line in tweets_topic:
    words = line.strip().lower().split()
    for word in words:
        if (word not in stopwords) and (word[0] != '#') and (word[0] != '@') and (word != ','):
            top_words[word] = top_words.get(word, 0) + 1

most_used_words = sorted(top_words, key=top_words.get, reverse=True)
count_u = 0
for word in most_used_words[:10]:
    print(top_words[word], word)