s# app.py
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    medications = conn.execute('SELECT * FROM medications ORDER BY time ASC').fetchall()
    conn.close()
    return render_template('index.html', medications=medications)

@app.route('/add', methods=['POST'])
def add_medication():
    name = request.form['med_name']
    dosage = request.form['med_dosage']
    time = request.form['med_time']
    frequency = request.form['med_freq']

    conn = get_db_connection()
    conn.execute('INSERT INTO medications (name, dosage, time, frequency) VALUES (?, ?, ?, ?)',
                 (name, dosage, time, frequency))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
