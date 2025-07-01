import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import os
base_path = os.path.abspath(os.path.dirname(__file__))
csv_path = os.path.join(base_path, '..', 'dataset', 'products.csv')
products = pd.read_csv(csv_path)

tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(products['description'])
similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

def recommend_products(product_id):
    idx = products.index[products['id'] == product_id][0]
    sim_scores = list(enumerate(similarity_matrix[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    product_indices = [i[0] for i in sim_scores]
    return products.iloc[product_indices].to_dict('records')
