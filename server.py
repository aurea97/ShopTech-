from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_order', methods=['POST'])
def add_order():
    product = request.form['product']
    
    conn = mysql.connector.connect(host='localhost', user='user', password='password', database='shoptech_db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO orders (product) VALUES (%s)", (product,))
    conn.commit()
    conn.close()
    
    return "Pedido agregado con éxito."

if __name__ == '__main__':
    app.run(debug=True)