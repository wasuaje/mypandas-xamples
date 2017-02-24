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

for index, row in movies.iterrows():
    #print(row['genres'].replace('|', ' '))
    YOUR_TEXT += row['genres'].replace('|', ',') + ','

YOUR_TEXT = YOUR_TEXT.replace('(no genres listed)', ',')
YOUR_TEXT = YOUR_TEXT.replace(',,,', ',')
YOUR_TEXT = YOUR_TEXT.replace(',', ' ')
# print(YOUR_TEXT)
counts = get_tag_counts(YOUR_TEXT)
# print(counts)
tags = make_tags(counts)

create_tag_image(tags, 'cloud_large.png', size=(450, 300), fontname='Lobster')
img = Image.open('cloud_large.png')
img.show()
