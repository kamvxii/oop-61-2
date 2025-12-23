import sqlite3

db = sqlite3.connect('users.db')
c=db.cursor()

#language=SQL
c.execute("""
CREATE TABLE users(
    name VARCHAR(50),
    age INTEGER,
    hobby TEXT
)
""")