from flask import Flask, request, redirect, jsonify
import sqlite3
import random
import string

app = Flask(__name__)

# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect('urls.db')
    conn.execute('CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY AUTOINCREMENT, short_code TEXT, long_url TEXT)')
    conn.commit()
    conn.close()

# Database connection
def get_db_connection():
    conn = sqlite3.connect('urls.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/shorten', methods=['POST'])
def shorten_url():
    long_url = request.json['long_url']
    # Generate a short code
    short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    conn = get_db_connection()
    conn.execute('INSERT INTO urls (short_code, long_url) VALUES (?, ?)', (short_code, long_url))
    conn.commit()
    conn.close()
    return jsonify({'short_url': f'http://localhost:5000/{short_code}'})

@app.route('/<short_code>')
def redirect_url(short_code):
    conn = get_db_connection()
    url = conn.execute('SELECT long_url FROM urls WHERE short_code = ?', (short_code,)).fetchone()
    conn.close()
    if url:
        return redirect(url['long_url'])
    return 'URL not found', 404

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
