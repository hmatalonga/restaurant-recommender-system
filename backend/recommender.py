#!/usr/bin/env python3

import sys
import pandas as pd
import numpy as np
from re import sub


params = {'cuisine': 'any food', 'price': 'any price', 'city': 'anywhere'}


def find_restaurant(df, cuisine=params['cuisine'], price=params['price'], city=params['city'], num=5):
    condition = None
    multiple = False

    if (cuisine != params['cuisine']):
        condition = df['Cuisine Style'].str.contains(
            cuisine.lower(), regex=False)
        multiple = True

    if (price != params['price']):
        if multiple:
            condition = condition & (df['Price Range'] == price.lower())
        else:
            condition = df['Price Range'] == price.lower()
            multiple = True

    if (city != params['city']):
        if multiple:
            condition = condition & (df['City'].str.lower() == city.lower())
        else:
            condition = df['City'].str.lower() == city.lower()

    gl = df[condition].sort_values(
        ['Ranking', 'Rating'], ascending=[True, False])

    cols = ['Name', 'City', 'Ranking', 'Rating', 'Price Range']

    return gl[cols].head(num)


def main():
    try:
        if len(sys.argv) < 2:
            raise IOError('Dataset missing!')

        df = pd.read_pickle(sys.argv[1])

        city = input('Enter city: ') or params['city']
        cuisine = input('Enter cuisine: ') or params['cuisine']
        price = input('Enter price: ') or params['price']

        print(find_restaurant(df, cuisine=cuisine,
                              city=city, price=price).to_string())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
