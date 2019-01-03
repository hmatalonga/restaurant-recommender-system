#!/usr/bin/env python3

import sys
import pandas as pd
from prepare import gen_sim_matrix
from recommender import params, simple_search, keyword_search


def main():
    try:
        if len(sys.argv) < 2:
            raise IOError('Dataset missing!')

        print('Loading dataset.')
        df = pd.read_pickle(sys.argv[1])

        print(df.head(10).to_string())

        print('Generating sim matrix.')
        cosine_func = gen_sim_matrix(df)

        mode = int(input('Search mode[1-2]: '))

        if (mode == 1):
            city = input('Enter city: ') or params['city']
            cuisine = input('Enter cuisine: ') or params['cuisine']
            price = input('Enter price: ') or params['price']

            results = simple_search(df, cuisine=cuisine,
                                    city=city, price=price, as_json=False)
            print(results.to_string())
        elif mode == 2:
            results = keyword_search(
                df, cosine_func, input('Restaurant name: '), as_json=False)
            print(results.to_string())
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
