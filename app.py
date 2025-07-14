from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)

DB_NAME = 'database.db'

# Buat koneksi ke database
def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# Inisialisasi DB jika belum ada
def init_db():
    if not os.path.exists(DB_NAME):
        conn = get_db_connection()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS medications (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                dosage TEXT NOT NULL,
                time TEXT NOT NULL,
                frequency TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

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

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_medication(id):
    conn = get_db_connection()
    if request.method == 'POST':
        name = request.form['med_name']
        dosage = request.form['med_dosage']
        time = request.form['med_time']
        frequency = request.form['med_freq']
        conn.execute('UPDATE medications SET name=?, dosage=?, time=?, frequency=? WHERE id=?',
                     (name, dosage, time, frequency, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    med = conn.execute('SELECT * FROM medications WHERE id=?', (id,)).fetchone()
    conn.close()
    return render_template('edit.html', med=med)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_medication(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM medications WHERE id=?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0')
