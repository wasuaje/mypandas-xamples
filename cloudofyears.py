# -*- coding: utf-8 -*-

from pytagcloud import create_tag_image, make_tags
from pytagcloud.lang.counter import get_tag_counts
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import matplotlib
import pylab
from PIL import Image

#
# USING A MODIFIED VERION OF counter.py from pytagcloud pack
#

DATA_FOLDER = 'ml-latest'
YOUR_TEXT = ""

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
        movie_years.append("None")

# print(movie_years)
# addd the serie itself
movies.loc[:, 'year'] = pd.Series(movie_years, index=movies.index)

years = " ".join(movie_years)

#movies_by_year = movies.groupby('year').size().sort_values()


# print(YOUR_TEXT)
counts = get_tag_counts(years)
# print(counts)
tags = make_tags(counts)

create_tag_image(tags, 'cloud_years.png', size=(450, 300), fontname='Lobster')
img = Image.open('cloud_years.png')
img.show()
