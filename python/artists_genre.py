# program to analyse spotify music
# santos borom 2021
# License: Creative Commons

from __future__ import absolute_import, division, print_function

import numpy as np
import pandas as pd
import re

artists_genres = pd.read_csv('/Users/playerone/Data/spotify/music_raw/data_w_genres.csv')

# print(artists_genres)
print('Artists & Genres:')
print(artists_genres.info())

# Artists & Genres:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 28680 entries, 0 to 28679
# Data columns (total 16 columns):
#  #   Column            Non-Null Count  Dtype  
# ---  ------            --------------  -----  
#  0   genres            28680 non-null  object 
#  1   artists           28680 non-null  object 
#  2   acousticness      28680 non-null  float64
#  3   danceability      28680 non-null  float64
#  4   duration_ms       28680 non-null  float64
#  5   energy            28680 non-null  float64
#  6   instrumentalness  28680 non-null  float64
#  7   liveness          28680 non-null  float64
#  8   loudness          28680 non-null  float64
#  9   speechiness       28680 non-null  float64
#  10  tempo             28680 non-null  float64
#  11  valence           28680 non-null  float64
#  12  popularity        28680 non-null  float64
#  13  key               28680 non-null  int64  
#  14  mode              28680 non-null  int64  
#  15  count             28680 non-null  int64  
# dtypes: float64(11), int64(3), object(2)

# print(artists_genres['genres'])

print(artists_genres.genres)

features_list = artists_genres.columns.tolist()

print(features_list)
# ['genres', 'artists', 'acousticness', 'danceability', 'duration_ms', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'valence', 'popularity', 'key', 'mode', 'count']

columns_reorder = ['artists', 'genres', 'popularity', 'valence',  'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'key', 'mode', 'duration_ms', 'count']

artists_genres = artists_genres.reindex(columns = columns_reorder)

print(artists_genres.artists)

print(artists_genres)

# properly escape double quote in artists names
artists_genres.artists = artists_genres.artists.apply(lambda x: x.replace('"', "'"))

print(artists_genres)

artists_genres = artists_genres.set_index('artists')

# print(type(artists_genres))

# genre names: take only names but leave [] empty genres
# for idx, text in enumerate(artists_genres.genres):
#     # print(text)
#     # print(idx)
#     string = re.search(r'\[(.*?)\]', text).group(1)
    
#     if string:
#         artists_genres['genres'][idx] = string


# artists_genres['genres'] = artists_genres['genres'].apply(lambda x: x.strip('[]'))

# now remove quote marks in genre names
# artists_genres['genres'] = artists_genres['genres'].apply(lambda x: x.replace("'",''))
# print(artists_genres.genres)

# save as csv
artists_genres.to_csv('/Users/playerone/Data/spotify/music_preprocessed/data_w_genres.csv')

# artists_genres = pd.read_csv('/Users/playerone/Data/music/data_w_genres.csv')

# print(artists_genres)
