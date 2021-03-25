# program to analyse spotify music
# santos borom 2021
# License: Creative Commons
from __future__ import absolute_import, division, print_function

import numpy as np
import pandas as pd
import re

genres = pd.read_csv('/Users/playerone/Data/spotify/music_raw/data_by_genres.csv')
print('Genres:')
print(genres.info())

# Genre:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 2973 entries, 0 to 2972
# Data columns (total 14 columns):
#  #   Column            Non-Null Count  Dtype  
# ---  ------            --------------  -----  
#  0   mode              2973 non-null   int64  
#  1   genres            2973 non-null   object 
#  2   acousticness      2973 non-null   float64
#  3   danceability      2973 non-null   float64
#  4   duration_ms       2973 non-null   float64
#  5   energy            2973 non-null   float64
#  6   instrumentalness  2973 non-null   float64
#  7   liveness          2973 non-null   float64
#  8   loudness          2973 non-null   float64
#  9   speechiness       2973 non-null   float64
#  10  tempo             2973 non-null   float64
#  11  valence           2973 non-null   float64
#  12  popularity        2973 non-null   float64
#  13  key               2973 non-null   int64  
# dtypes: float64(11), int64(2), object(1)

# print(genre_types.columns)
# # Index(['mode', 'genres', 'acousticness', 'danceability', 'duration_ms',
# #        'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness',
# #        'tempo', 'valence', 'popularity', 'key'],
# #       dtype='object')


features_list = genres.columns.tolist()

print(features_list)

# ['mode', 'genres', 'acousticness', 'danceability', 'duration_ms', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'valence', 'popularity', 'key']

columns_reorder = ['genres', 'popularity', 'valence',  'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'key', 'mode', 'duration_ms']

genres = genres.reindex(columns = columns_reorder)

print(genres)

genres.set_index('genres', inplace=True)

genres.to_csv('/Users/playerone/Data/spotify/music_preprocessed/data_by_genres.csv')