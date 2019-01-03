#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
from re import sub
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def gen_sim_matrix(df, col_name='keyword', lang='english'):
    # Import CountVectorizer and create the count matrix
    count = CountVectorizer(stop_words=lang)
    count_matrix = count.fit_transform(df[col_name])
    # Compute the Cosine Similarity matrix based on the count_matrix
    return cosine_similarity(count_matrix, count_matrix)


def main():
    try:
        if len(sys.argv) < 2:
            raise IOError('Dataset missing!')

        df = pd.read_csv(sys.argv[1], encoding='latin1')

        df = df.iloc[:, 1:].copy()
        df = df.dropna()

        df = df.sample(20000)

        df['City'] = df['City'].str.capitalize()
        df['Cuisine Style'] = df['Cuisine Style'].str.lower()
        df['keyword'] = df['keyword'].str.lower()
        df['keyword'] = df['keyword'].str.strip()

        df['Cuisine Style'] = df['Cuisine Style'].apply(
            lambda x: ' '.join(x.split(',')).split())
        df['keyword'] = df['keyword'].apply(lambda x: sub(' +', ' ', x))

        df = df.sort_values(['Ranking', 'Rating'], ascending=[True, False])

        df.to_pickle('./data/dataset.pkl')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
