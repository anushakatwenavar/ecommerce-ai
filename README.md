# 🛍️ AI-Powered E-Commerce App

An intelligent product recommendation web application built with **Python**, **Flask**, and **Machine Learning**. Users can register, log in, browse products, add items to their cart, and get AI-powered product recommendations based on a CSV dataset.

---

## 🔍 Features

- 🧠 AI-based Product Recommender
- 📝 User Registration & Login
- 🛒 Cart Management
- 💡 Product Display with Add-to-Cart
- 📦 Flask Backend + Pandas Dataset

---

## 📁 Project Structure

ecommerce-ai/
│
├── app/
│ ├── main.py
│ ├── routes.py
│ ├── recommender.py
│ ├── auth.py
│ ├── templates/
│ │ ├── index.html
│ │ ├── login.html
│ │ ├── register.html
│ │ ├── cart.html
│ │ └── product.html
│ └── static/
│ └── (CSS, JS, images if any)
│
├── dataset/
│ └── products.csv
│
├── venv/
├── requirements.txt
└── README.md

---

## 🧠 Tech Stack

- **Python 3.7+**
- **Flask**
- **Pandas**
- **HTML / CSS (Jinja2)**
- **Git + GitHub**

---

## 🚀 Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/anushakatwenavar/ecommerce-ai.git
cd ecommerce-ai

# 2. Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
python app/main.py

## 📸 Screenshots

### 🏠 Homepage
![Homepage](Screenshots/Screenshot (3) - Copy.png)

### 🔐 Login Page
![Login](screenshots/Screenshot (4).png)

### 🛍️ Product Listing
![Products](screenshots/Screenshot (5).png)

### 🛒 Cart
![Cart](screenshots/Screenshot (6).png)






