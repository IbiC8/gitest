import json
import sqlite3

conn=sqlite3.connect('many.sqlite')
cur=conn.cursor()

cur.executescript('''DROP TABLE IF EXISTS User ;
DROP TABLE IF EXISTS Course ;
DROP TABLE IF EXISTS Member ''')

cur.execute('CREATE TABLE User (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, name TEXT UNIQUE)')
cur.execute('CREATE TABLE Course (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, title VARCHAR )')
cur.execute('CREATE TABLE Member (user_id INTEGER, course_id INTEGER, role INTEGER, PRIMARY KEY (user_id, course_id))')

file=input('Enter roster:\n')
dat=open(file).read()
data=json.loads(dat)

for x in data:
    nam=x[0]
    titl=x[1]
    rol=x[2]

    cur.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (nam,))
    cur.execute('SELECT id FROM User WHERE name= (?)', (nam,))
    user_id=cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (titl,))
    cur.execute('SELECT id FROM Course WHERE title =(?)', (titl,))
    course_id=cur.fetchone()[0]

    cur.execute('INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES (?,?,?)', (user_id, course_id, rol))

    conn.commit()

print('done')
