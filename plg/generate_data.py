import pandas as pd
import numpy as np
import sys
import os.path

# def kgrams_hash(sentence, k=5):
    # hashes = []
    # words = nltk.word_tokenize(sentence)
    # for i in range(0, len(words) - k + 1):
        # mystring = ' '.join(words[i:i+k])
        # hash_object = hashlib.md5(mystring.encode())
        # hsh = hash_object.hexdigest()
        # hashes.append(hsh)
    # return hashes

# def winnow(text, k=5, w=6):
    # fingerprints = set([])
    # sentences = nltk.sent_tokenize(text)
    # dic = {}
    # for index, sentence in enumerate(sentences):
        # sentence_hashes = kgrams_hash(sentence, k)
        # if len(sentence_hashes) and len(sentence_hashes) < w:
            # fingerprints.add(min(sentence_hashes))
        # else:
            # for i in range(0, len(sentence_hashes) - w + 1):
                # window = sentence_hashes[i:i+w]
                # fingerprints.add(min(window))
    # return fingerprints

df = pd.read_json('temp.json', lines=True)
ratings = df['overall']
num_reviews = ratings.size
helpfulness = df['helpful']
min_helpfull_review = 10
temp = [i for i in range(num_reviews)  if helpfulness[i][1] > min_helpfull_review]
df_temp = df.iloc[temp].reset_index()
df = df_temp

print "Number of reviews with helpfulness > 10 = ", len(temp)
# print os.path.exists('data.pkl')
if (os.path.exists('data.pkl')):
    df2 = pd.read_pickle('data.pkl')
    df2 = pd.concat([df2, df], ignore_index=True)
    # df2.reset_index(drop=True)
    df2.to_pickle('data.pkl')
else:
    print "No pickle file exists currently"
    df.to_pickle('data.pkl')

