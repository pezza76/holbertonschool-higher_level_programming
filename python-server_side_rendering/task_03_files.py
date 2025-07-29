
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
    source = request.args.get('source')
    id = request.args.get('id')
    
    if source == 'json':
        with open('products.json') as f:
            items = json.load(f)
    
    elif source == 'csv':
        with open('products.csv') as f:
            data = csv.DictReader(f)
            items = list(data)

    else:
        return "Wrong source", 200



    if id:
        items = [item for item in items if str(item.get('id')) == id]
        if not items:
            return "Product not found", 200
    
            
            
    return render_template('product_display.html', items=items)


if __name__ == "__main__":
    app.run(debug=True)