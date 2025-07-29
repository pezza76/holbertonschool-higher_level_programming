
from flask import Flask, render_template, json, request
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/items')
def items():
    with open('items.json') as f:
        data = json.load(f)
    return render_template('items.html', items = data.get('items', []))

@app.route('/products')
def products():
    
    if request.args.get('source') == 'json':
        with open('products.json') as f:
            data = json.load(f)
        return render_template('product_display.html', items = data)
    
    elif request.args.get('source') == 'csv':
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            data = list(reader)
        return render_template('product_display.html', items = data)
    
    return "Wrong source", 200

if __name__ == "__main__":
    app.run(debug=True)