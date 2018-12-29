#!/usr/bin/env python3

import pandas as pd
import numpy as np
from ast import literal_eval
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Function to convert all strings to lower case and strip names of spaces
def clean_data(x):
    if isinstance(x, list):
        return [str.lower(i.replace(" ", "")) for i in x]
    else:
        if isinstance(x, str):
            return str.lower(x.replace(" ", ""))
        else:
            return ''


# Function that takes in movie title as input and outputs most similar movies
def get_recommendations(title, indices, cosine_sim, num=10):
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwsie similarity scores of all movies with that movie
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the scores of the 10 most similar movies
    sim_scores = sim_scores[1:num+1]

    # Get the restaurants indices
    restaurants_indices = [i[0] for i in sim_scores]

    # Return the top 10 most similar movies
    return df['Name'].iloc[restaurants_indices]


print('Reading dataset...')
df = pd.read_csv('../data/TA_restaurants_curated.csv', encoding='utf-8')
df = df.iloc[:, 1:7].copy()
df = df.sample(100000)

print('Cleaning data...')
df = df.dropna()
df['Price Range'] = df['Price Range'].astype('category')

for feature in ['City', 'Cuisine Style']:
    df[feature] = df[feature].apply(clean_data)

# Parse the stringified features into their corresponding python objects
for feature in ['Cuisine Style']:
    df[feature] = df[feature].apply(literal_eval)

print('Preparing soup...')
df['soup'] = df.apply(lambda x: ' '.join(
    x['Cuisine Style']) + ' ' + x['City'], axis=1)

print('Making count matrix...')
# Import CountVectorizer and create the count matrix
count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(df['soup'])

print('Calculating cosine similarity...')
cosine_sim = cosine_similarity(count_matrix, count_matrix)

print('Resetting indexes...')
df = df.reset_index()
indices = pd.Series(df.index, index=df['Name'])

print('Example input: ', indices[50])

restaurant_name = input('Restaurant Name: ')
recommendations = get_recommendations(restaurant_name, indices, cosine_sim)

print(recommendations)
