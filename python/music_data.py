# program to analyse spotify music
# santos borom 2021
# License: Creative Commons

from __future__ import absolute_import, division, print_function

import numpy as np
import pandas as pd
import re

music_data = pd.read_csv('/Users/playerone/Data/spotify/music_raw/data.csv')


print('Music data:')
print(music_data.info())
print(music_data.artists)

# Music data:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 170653 entries, 0 to 170652
# Data columns (total 19 columns):
#  #   Column            Non-Null Count   Dtype  
# ---  ------            --------------   -----  
#  0   valence           170653 non-null  float64
#  1   year              170653 non-null  int64  
#  2   acousticness      170653 non-null  float64
#  3   artists           170653 non-null  object 
#  4   danceability      170653 non-null  float64
#  5   duration_ms       170653 non-null  int64  
#  6   energy            170653 non-null  float64
#  7   explicit          170653 non-null  int64  
#  8   id                170653 non-null  object 
#  9   instrumentalness  170653 non-null  float64
#  10  key               170653 non-null  int64  
#  11  liveness          170653 non-null  float64
#  12  loudness          170653 non-null  float64
#  13  mode              170653 non-null  int64  
#  14  name              170653 non-null  object 
#  15  popularity        170653 non-null  int64  
#  16  release_date      170653 non-null  object 
#  17  speechiness       170653 non-null  float64
#  18  tempo             170653 non-null  float64
# dtypes: float64(9), int64(6), object(4)

# column_names = ["C", "A", "B"]
# df = df.reindex(columns=column_names)

# get the column names
print('The column names:', music_data.columns)

features_list = music_data.columns.tolist()

print(features_list)

# columns_default = ['valence', 'year', 'acousticness', 'artists', 'danceability', 'duration_ms', 'energy', 'explicit', 'id', 'instrumentalness', 'key', 'liveness', 'loudness', 'mode', 'name', 'popularity', 'release_date', 'speechiness', 'tempo']

columns_reorder = ['id', 'name', 'artists', 'popularity', 'year', 'release_date', 'valence',  'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'key', 'mode', 'explicit', 'duration_ms']

# reorder the columns
music_data = music_data.reindex(columns = columns_reorder)

print(music_data)

# set new index
music_data.set_index('id', inplace=True)

print(music_data)

# music_data['artists'] = music_data['artists'].apply(lambda x: x.strip('[]'))
# print(music_data.artists)

# for idx, text in enumerate(music_data.artists):
#     # print(text)
#     # print(idx)
#     string = re.search(r'\[(.*?)\]', text).group(1)
    
#     if string:
#         music_data['artists'][idx] = string

# music_data['artists'] = music_data['artists'].apply(lambda x: x.replace("'",''))

# print(music_data.artists)

music_data.to_csv('/Users/playerone/Data/spotify/music_preprocessed/data.csv')

# music_data = pd.read_csv('/Users/playerone/Data/spotify/music_preprocessed/data.csv')

# print(music_data)