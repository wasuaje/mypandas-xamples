# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import matplotlib
import pylab

DATA_FOLDER = 'ml-latest'

m_cols = ['movieId', 'title', 'genres']
movies = pd.read_csv(DATA_FOLDER + '/movies.csv', sep=',', names=m_cols,
                     encoding='latin-1', header=1)

movie_years = []

# create a serie for the movie year
for index, row in movies.iterrows():
    # print(row['movieId'], row['title'])
    re_year = re.compile('.*\((\d{4})\).*')
    # print(re_year)
    year = re_year.match(row['title'])
    if year:
        movie_years.append(year.group(1))
        # print(year.group(1))
    else:
        movie_years.append(None)

# print(movie_years)
# addd the serie itself
movies.loc[:, 'year'] = pd.Series(movie_years, index=movies.index)

# print(movies.tail())

movies_by_year = movies.groupby('year').size().sort_values()

# print(movies_by_year.values)
# plt.figure()
# movies_by_year.plot(style='k--', label='Series')
ts = pd.Series(
    movies_by_year.values,
    index=movies_by_year.index)
#ts = ts.cumsum()
# print(ts)

mpl = ts.plot(label='Years')
#mpl.ylabel('some numbers')
pylab.show()
