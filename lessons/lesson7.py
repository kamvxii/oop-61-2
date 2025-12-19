import sqlite3

db = sqlite3.connect('itproger.db')
c=db.cursor()
c.execute('''CREATE TABLE student (title text
)''')
