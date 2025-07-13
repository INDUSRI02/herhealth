import sqlite3
import hashlib

conn = sqlite3.connect('backend/database.db', check_same_thread=False)
c = conn.cursor()

def create_user_table():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT, password TEXT)')

def add_user(username, password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)', (username, password))
    conn.commit()

def login_user(username, password):
    c.execute('SELECT * FROM userstable WHERE username = ? AND password = ?', (username, password))
    return c.fetchall()

def hash_password(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def create_prediction_table():
    c.execute('''
        CREATE TABLE IF NOT EXISTS prediction_logs (
            username TEXT,
            age INTEGER,
            weight REAL,
            height REAL,
            cycle_length INTEGER,
            irregular_periods INTEGER,
            facial_hair INTEGER,
            acne INTEGER,
            hair_loss INTEGER,
            dark_patches INTEGER,
            predicted_risk TEXT
        )
    ''')
    conn.commit()

def log_prediction(username, age, weight, height, cycle_length,
                   irregular_periods, facial_hair, acne, hair_loss,
                   dark_patches, risk_level):
    c.execute('''
        INSERT INTO prediction_logs VALUES (?,?,?,?,?,?,?,?,?,?,?)
    ''', (username, age, weight, height, cycle_length,
          irregular_periods, facial_hair, acne, hair_loss,
          dark_patches, risk_level))
    conn.commit()
