#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
from re import sub


def main():
    try:
        if len(sys.argv) < 2:
            raise IOError('Dataset missing!')

        df = pd.read_csv(sys.argv[1], encoding='latin1')

        df = df.iloc[:, 1:].copy()
        df = df.dropna()

        df['City'] = df['City'].str.capitalize()
        df['Cuisine Style'] = df['Cuisine Style'].str.lower()
        df['keyword'] = df['keyword'].str.lower()
        df['keyword'] = df['keyword'].str.strip()

        df['Cuisine Style'] = df['Cuisine Style'].apply(
            lambda x: ' '.join(x.split(',')).split())
        df['keyword'] = df['keyword'].apply(lambda x: sub(' +', ' ', x))

        df = df.sort_values(['Ranking', 'Rating'], ascending=[True, False])

        df.to_pickle('../data/dataset.pkl')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
