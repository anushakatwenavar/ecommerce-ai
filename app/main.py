from flask import Flask, render_template
from routes import main
from auth import auth, init_db   # ✅ Make sure this line is present
from cart import cart_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.register_blueprint(main)     # ✅ Needed for your main site
app.register_blueprint(auth)     # ✅ Needed for /login, /register
from cart import cart_bp
app.register_blueprint(cart_bp)


init_db()

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
