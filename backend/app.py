import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from recommender import params, simple_search, keyword_search
from prepare import gen_sim_matrix

app = Flask(__name__)
CORS(app)
df = None
cosine_func = None


@app.route('/', methods=['GET'])
def entry():
    return jsonify(message='Ready')


@app.route('/simple', methods=['GET'])
def simple():
    cuisine = request.args.get('cuisine', params['cuisine'])
    price = request.args.get('price', params['price'])
    city = request.args.get('city', params['city'])

    print('Simple search for: ', cuisine, price, city)

    results = simple_search(df, cuisine=cuisine, price=price, city=city)
    return jsonify(results)


@app.route('/keyword', methods=['GET'])
def keyword():
    searchword = request.args.get('name', '')

    if searchword == '':
        return jsonify(message='Provide a restaurant name.')

    print('Keyword search for: ', searchword)

    results = keyword_search(df, cosine_func, searchword)
    return jsonify(results)


if __name__ == '__main__':
    print('Loading dataset.')
    df = pd.read_pickle('./data/dataset.pkl')
    print('Generating sim matrix')
    cosine_func = gen_sim_matrix(df)
    app.run(host='0.0.0.0', port=80)
