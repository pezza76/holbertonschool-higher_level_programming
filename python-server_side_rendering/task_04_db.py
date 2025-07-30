
from flask import Flask, render_template, json, request
import csv
import sqlite3

def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('''
        INSERT OR IGNORE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    conn.commit()
    conn.close()

app = Flask(__name__)
create_database()

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

    elif source == 'sql':
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()

        if id:
            cursor.execute("SELECT * FROM Products WHERE id = ?", (id,))
        else:
            cursor.execute("SELECT * FROM Products")
        
        rows = cursor.fetchall()
        conn.close()

        items = [
    {'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]}
    for row in rows]



        
    else:
        return "Wrong source", 200



    if id:
        items = [item for item in items if str(item.get('id')) == id]
        if not items:
            return "Product not found", 200
    
            
            
    return render_template('product_display.html', items=items)


if __name__ == "__main__":
    app.run(debug=True)