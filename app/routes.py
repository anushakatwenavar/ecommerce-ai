from flask import Blueprint, render_template
from recommender import recommend_products

main = Blueprint('main', __name__)  # ✅ THIS LINE must be present

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/product/<int:product_id>')
def product(product_id):
    recommendations = recommend_products(product_id)
    return render_template('product.html', recommendations=recommendations)
