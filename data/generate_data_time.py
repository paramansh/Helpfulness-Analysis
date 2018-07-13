import pandas as pd
import numpy as np
import sys
import os.path

df = pd.read_json('temp.json', lines=True)
df = df[['overall', 'asin', 'helpful', 'unixReviewTime']]
# print os.path.exists('data.pkl')
if (os.path.exists('data.pkl')):
    df2 = pd.read_pickle('data.pkl')
    df2 = pd.concat([df2, df], ignore_index=True)
    # df2.reset_index(drop=True)
    df2.to_pickle('data.pkl')
else:
    print "No pickle file exists currently"
    df.to_pickle('data.pkl')

