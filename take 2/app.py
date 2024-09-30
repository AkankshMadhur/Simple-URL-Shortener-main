import sqlite3
import string
import random
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# Connect to SQLite database
def init_db():
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, original TEXT, short TEXT)''')
    conn.commit()
    conn.close()

# Shorten the URL
def shorten_url(original_url):
    characters = string.ascii_letters + string.digits
    short_url = ''.join(random.choices(characters, k=6))  # Generate a 6-character string
    return short_url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form['url']
        short_url = shorten_url(original_url)
        
        # Save to database
        conn = sqlite3.connect('urls.db')
        c = conn.cursor()
        c.execute("INSERT INTO urls (original, short) VALUES (?, ?)", (original_url, short_url))
        conn.commit()
        conn.close()
        
        return f'Shortened URL: <a href="/{short_url}">/{short_url}</a>'
    
    return render_template('index.html')

@app.route('/<short_url>')
def redirect_to_url(short_url):
    conn = sqlite3.connect('urls.db')
    c = conn.cursor()
    c.execute("SELECT original FROM urls WHERE short=?", (short_url,))
    result = c.fetchone()
    conn.close()
    
    if result:
        return redirect(result[0])
    else:
        return "URL not found", 404

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
