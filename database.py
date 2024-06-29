import sqlite3
from flask import g

def connect_to_database():
    if 'db' not in g:
        g.db = sqlite3.connect('greenAge.db')

def get_database():
    if 'db' not in g:
        connect_to_database()
    return g.db

def close_connection():
    db = g.pop('db', None)
    if db is not None:
        db.close()

# User table operations

def create_user(email, name, phone, cfp, region):
    db = get_database()
    cursor = db.cursor()
    cursor.execute('''INSERT INTO user (email, name, phone, cfp, region) 
                    VALUES (?, ?, ?, ?, ?)''', (email, name, phone, cfp, region))
    db.commit()

def fetch_users():
    db = get_database()
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM user''')
    rows = cursor.fetchall()
    return rows

def update_user(email, name, phone, cfp, region):
    db = get_database()
    cursor = db.cursor()
    cursor.execute('''UPDATE user SET name=?, phone=?, cfp=?, region=? WHERE email=?''', 
                   (name, phone, cfp, region, email))
    db.commit()

def delete_user(email):
    db = get_database()
    cursor = db.cursor()
    cursor.execute('''DELETE FROM user WHERE email=?''', (email,))
    db.commit()

# Social table operations

def create_social_post(email, post, sentiment, date):
    db = get_database()
    cursor = db.cursor()
    cursor.execute('''INSERT INTO social (email, post, sentiment, date) 
                    VALUES (?, ?, ?, ?)''', (email, post, sentiment, date))
    db.commit()

def fetch_social_posts():
    db = get_database()
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM social''')
    rows = cursor.fetchall()
    return rows

def update_social_post(email, post, sentiment, date):
    db = get_database()
    cursor = db.cursor()
    cursor.execute('''UPDATE social SET post=?, sentiment=?, date=? WHERE email=?''', 
                   (post, sentiment, date, email))
    db.commit()

def delete_social_post(email, date):
    db = get_database()
    cursor = db.cursor()
    cursor.execute('''DELETE FROM social WHERE email=? AND date=?''', (email, date))
    db.commit()

# Additional functions:

def fetch_table_names():
    db = get_database()
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    return tables
