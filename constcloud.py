# -*- coding: utf-8 -*-

from pytagcloud.lang.stopwords import StopWords
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


DATA_FOLDER = 'const'

with open(DATA_FOLDER + '\const.txt', 'r', encoding='utf-8') as myfile:
    YOUR_TEXT = myfile.read().replace('\n', '')

# print(YOUR_TEXT)
counts = get_tag_counts(YOUR_TEXT, 'spanish')
print(counts)
tags = make_tags(counts[:100])
# print(tags)
create_tag_image(tags, 'cloud_const.png', size=(800, 600), fontname='Lobster')
img = Image.open('cloud_const.png')
img.show()
