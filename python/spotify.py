# program to analyse spotify music
# santos borom 2021
# License: Creative Commons

from __future__ import absolute_import, division, print_function

import numpy as np
import pandas as pd
import re

music_data = pd.read_csv('/Users/playerone/Data/music/data.csv')


print('Music data:')
print(music_data.info())
print(music_data.artists)

# music_data['artists'] = music_data['artists'].apply(lambda x: x.strip('[]'))
# print(music_data.artists)

for idx, text in enumerate(music_data.artists):
    # print(text)
    # print(idx)
    string = re.search(r'\[(.*?)\]', text).group(1)
    
    if string:
        music_data['artists'][idx] = string

music_data['artists'] = music_data['artists'].apply(lambda x: x.strip("''"))

print(music_data.artists)

music_data.to_csv('/Users/playerone/Data/music/data.csv')

music_data = pd.read_csv('/Users/playerone/Data/music/music_data.csv')

print(music_data)

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

print(music_data.columns)
# Index(['valence', 'year', 'acousticness', 'artists', 'danceability',
#        'duration_ms', 'energy', 'explicit', 'id', 'instrumentalness', 'key',
#        'liveness', 'loudness', 'mode', 'name', 'popularity', 'release_date',
#        'speechiness', 'tempo'],
#       dtype='object')


artists = pd.read_csv('/Users/playerone/Data/music/data_by_artist.csv')
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
#       dtype='object')

artists_genres = pd.read_csv('/Users/playerone/Data/music/data_w_genres.csv')

#print(artists_genres)
print('Artists & Genres:')
print(artists_genres.info())

# artists_genres['genres'] = artists_genres['genres'].apply(lambda x: x.strip('[]'))
# print(artists_genres.genres)

print(artists_genres['genres'])

for idx, text in enumerate(artists_genres.genres):
    # print(text)
    # print(idx)
    string = re.search(r'\[(.*?)\]', text).group(1)
    
    if string:
        artists_genres['genres'][idx] = string

print(artists_genres.genres)


artists_genres.to_csv('/Users/playerone/Data/music/data_w_genres.csv')

artists_genres = pd.read_csv('/Users/playerone/Data/music/data_w_genres.csv')

print(artists_genres)

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

print(artists_genres.columns)
# Index(['genres', 'artists', 'acousticness', 'danceability', 'duration_ms',
#        'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness',
#        'tempo', 'valence', 'popularity', 'key', 'mode', 'count'],
#       dtype='object')



genre_types = pd.read_csv('/Users/playerone/Data/music/data_by_genres.csv')
print('Genre:')
print(genre_types.info())

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

year_overall = pd.read_csv('/Users/playerone/Data/music/data_by_year.csv')
print('The Years:')
print(year_overall.info())

# The Years:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 100 entries, 0 to 99
# Data columns (total 14 columns):
#  #   Column            Non-Null Count  Dtype  
# ---  ------            --------------  -----  
#  0   mode              100 non-null    int64  
#  1   year              100 non-null    int64  
#  2   acousticness      100 non-null    float64
#  3   danceability      100 non-null    float64
#  4   duration_ms       100 non-null    float64
#  5   energy            100 non-null    float64
#  6   instrumentalness  100 non-null    float64
#  7   liveness          100 non-null    float64
#  8   loudness          100 non-null    float64
#  9   speechiness       100 non-null    float64
#  10  tempo             100 non-null    float64
#  11  valence           100 non-null    float64
#  12  popularity        100 non-null    float64
#  13  key               100 non-null    int64  
# dtypes: float64(11), int64(3)

# print(year_overall.columns)
# Index(['mode', 'year', 'acousticness', 'danceability', 'duration_ms', 'energy',
#        'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo',
#        'valence', 'popularity', 'key'],
#       dtype='object')

