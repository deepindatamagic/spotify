# program to analyse spotify music
# santos borom 2021
# License: Creative Commons
from __future__ import absolute_import, division, print_function

import numpy as np
import pandas as pd
import re

artists = pd.read_csv('/Users/playerone/Data/music/music/data_by_artist.csv')
print('The Artists:')
print(artists.info())

# The Artists:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 28680 entries, 0 to 28679
# Data columns (total 15 columns):
#  #   Column            Non-Null Count  Dtype  
# ---  ------            --------------  -----  
#  0   mode              28680 non-null  int64  
#  1   count             28680 non-null  int64  
#  2   acousticness      28680 non-null  float64
#  3   artists           28680 non-null  object 
#  4   danceability      28680 non-null  float64
#  5   duration_ms       28680 non-null  float64
#  6   energy            28680 non-null  float64
#  7   instrumentalness  28680 non-null  float64
#  8   liveness          28680 non-null  float64
#  9   loudness          28680 non-null  float64
#  10  speechiness       28680 non-null  float64
#  11  tempo             28680 non-null  float64
#  12  valence           28680 non-null  float64
#  13  popularity        28680 non-null  float64
#  14  key               28680 non-null  int64  
# dtypes: float64(11), int64(3), object(1)

print(artists.columns)
# Index(['mode', 'count', 'acousticness', 'artists', 'danceability',
#        'duration_ms', 'energy', 'instrumentalness', 'liveness', 'loudness',
#        'speechiness', 'tempo', 'valence', 'popularity', 'key'],


#print(artists)
print('Artists:')
print(artists.info())

# properly escape double quote in artists names
artists['artists'] = artists['artists'].apply(lambda x: x.replace('"', "'"))

# artists['artists'] = artists['artists'].apply(lambda x: x.strip('[]'))
# print(artists.artists)

# print(artists['artists'])

# for idx, text in enumerate(artists.artists):
#     # print(text)
#     # print(idx)
#     string = re.search(r'\[(.*?)\]', text).group(1)
    
#     if string:
#         artists['artists'][idx] = string

# print(artists.artists)

artists.to_csv('/Users/playerone/Data/music/data_by_artists.csv')

artists = pd.read_csv('/Users/playerone/Data/music/data_by_artists.csv')

print(artists)