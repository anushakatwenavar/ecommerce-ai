# app/cart.py
from flask import Blueprint, session, redirect, url_for, request, render_template, flash

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/add_to_cart/<product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', [])
    cart.append(product_id)
    session['cart'] = cart
    flash(f'Added product #{product_id} to cart.')
    return redirect(url_for('index'))

@cart_bp.route('/cart')
def view_cart():
    cart = session.get('cart', [])
    return render_template('cart.html', cart=cart)

@cart_bp.route('/remove_from_cart/<product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    if product_id in cart:
        cart.remove(product_id)
        session['cart'] = cart
        flash(f'Removed product #{product_id} from cart.')
    return redirect(url_for('cart.view_cart'))
