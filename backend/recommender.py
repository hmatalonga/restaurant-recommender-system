#!/usr/bin/env python3

import pandas as pd
import numpy as np


params = {'cuisine': 'any food', 'price': 'any price', 'city': 'anywhere'}


def simple_search(df, cuisine=params['cuisine'], price=params['price'], city=params['city'], num=5, as_json=True):
    gl = None
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

    if as_json:
        return gl[cols].head(num).to_json(orient='records')
    else:
        return gl[cols].head(num)


def keyword_search(df, sim_func, name, index_name='Name', num=5, as_json=True):
    df = df.reset_index()
    indices = pd.Series(df.index, index=df[index_name])

    # Get the index of the movie that matches the title
    idx = indices[name]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(sim_func[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:num+1]

    # Get the restaurants indices
    result_indices = [i[0] for i in sim_scores]

    # Return the top results
    recommendations = df[index_name].iloc[result_indices]
    cols = ['Name', 'City', 'Ranking', 'Rating', 'Price Range']
    subset = df[df[index_name].isin(recommendations)]

    if as_json:
        return subset[cols].head(num).to_json(orient='records')
    else:
        return subset[cols].head(num)
