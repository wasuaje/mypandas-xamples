# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
DATA_FOLDER = 'ml-latest'

# pass in column names for each CSV
# u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
# users = pd.read_csv(DATA_FOLDER+'/u.user', sep='|', names=u_cols,
#                    encoding = 'latin-1')

r_cols = ['userId', 'movieId', 'rating', 'timestamp']
ratings = pd.read_csv(DATA_FOLDER + '/ratings.csv', sep=',', names=r_cols,
                      encoding='latin-1', header=1)

# the movies file contains columns indicating the movie's genres
# let's only load the first five columns of the file with usecols
m_cols = [
    'movieId',
    'title',
    'genres',
]

movies = pd.read_csv(DATA_FOLDER + '/movies.csv', sep=',', names=m_cols,
                     encoding='latin-1', header=1)

# create one merged DataFrame
movie_ratings = pd.merge(movies, ratings)
#lens = pd.merge(movie_ratings, users)

most_rated = movie_ratings.groupby(
    'title').size().sort_values(ascending=False)[:25]

print(most_rated)

g_cols = ['tagId', 'tag']

# genome_tags = pd.read_csv(DATA_FOLDER + '/genome-tags.csv', sep=',', names=g_cols,
#                          encoding='latin-1', header=1)

gs_cols = ['movieId', 'tagId', 'relevance']
# genome_scores = pd.read_csv(DATA_FOLDER + '/genome-scores.csv', sep=',', names=gs_cols,
#                           encoding='latin-1', header=1)

#gs_scores = pd.merge(genome_scores, genome_tags)

# print(gs_scores[:25])

# most_rated = gs_scores.groupby('tag').agg(
#    {'relevance': [np.mean]})


# most_rated = gs_scores.tag.value_counts()[:25]

# print(most_rated.sort_values([('relevance', 'mean')], ascending=False)[:25])
