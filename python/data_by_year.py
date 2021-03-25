# program to analyse spotify music
# santos borom 2021
# License: Creative Commons
from __future__ import absolute_import, division, print_function

import numpy as np
import pandas as pd
import re

years = pd.read_csv('/Users/playerone/Data/spotify/music_raw/data_by_year.csv')
print('The Years:')
print(years.info())

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


features_list = years.columns.tolist()

print(features_list)
# ['mode', 'year', 'acousticness', 'danceability', 'duration_ms', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'valence', 'popularity', 'key']

columns_reorder = ['year', 'popularity', 'valence', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'key', 'mode']

years = years.reindex(columns = columns_reorder)

print(years)

years.set_index('year', inplace=True)

years.to_csv('/Users/playerone/Data/spotify/music_preprocessed/data_by_year.csv')