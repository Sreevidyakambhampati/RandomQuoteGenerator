# app.py
from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Define a list of quotes with authors
quotes = [
    {"quote": "The greatest glory in living lies not in never falling, but in rising every time we fall.", "author": "Nelson Mandela"},
    {"quote": "The way to get started is to quit talking and begin doing.", "author": "Walt Disney"},
    {"quote": "Your time is limited, don't waste it living someone else's life.", "author": "Steve Jobs"},
    # Add more quotes as needed
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quote')
def quote():
    quote = random.choice(quotes)
    return jsonify(content=quote['quote'], author=quote['author'])

if __name__ == '__main__':
    app.run(debug=True)
