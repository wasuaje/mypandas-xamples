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

DATA_FOLDER = 'bible'

with open(DATA_FOLDER + '\pg10.txt', 'r', encoding='utf-8') as myfile:
    YOUR_TEXT = myfile.read().replace('\n', '')

# print(YOUR_TEXT)
counts = get_tag_counts(YOUR_TEXT, 'english')
print(counts)
tags = make_tags(counts[:100])
# print(tags)
create_tag_image(tags, 'cloud_bible.png', size=(800, 600), fontname='Lobster')
img = Image.open('cloud_bible.png')
img.show()
