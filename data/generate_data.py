import pandas as pd
import numpy as np
import sys
import os.path

df = pd.read_json('temp.json', lines=True)
ratings = df['overall']
num_reviews = ratings.size
helpfulness = df['helpful']
min_helpfull_review = 5
temp = [i for i in range(num_reviews)  if helpfulness[i][1] > min_helpfull_review]
df_temp = df[['asin', 'helpful', 'overall', 'reviewerID']].iloc[temp].reset_index()
df = df_temp

print "Number of reviews with helpfulness > 5 = ", len(temp)
# print os.path.exists('data.pkl')
if (os.path.exists('data.pkl')):
    df2 = pd.read_pickle('data.pkl')
    df2 = pd.concat([df2, df], ignore_index=True)
    # df2.reset_index(drop=True)
    df2.to_pickle('data.pkl')
else:
    print "No pickle file exists currently"
    df.to_pickle('data.pkl')

