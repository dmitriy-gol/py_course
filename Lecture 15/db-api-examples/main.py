Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import sqlite3
conn = sqlite3.connect("todo.db")
print(type(conn))
<class 'sqlite3.Connection'>

c = conn.cursor()
print(type(c))
<class 'sqlite3.Cursor'>

c.execute("""CREATE TABLE IF NOT EXISTS tasks (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
priority INTEGER NOT NULL
);""")
<sqlite3.Cursor object at 0x00000195FA2083C0>
c.execute("INSERT INTO tasks (name, priority) VALUES (?,?)", ("My first task", 1))
<sqlite3.Cursor object at 0x00000195FA2083C0>
conn.commit()

tasks = [
   ("My new task", 15),
   ("My second task", 5),
   ("My third task", 10),
]

c.executemany("INSERT INTO tasks (name, priority) VALUES (?,?)", tasks)
<sqlite3.Cursor object at 0x00000195FA2083C0>
conn.commit()

for row in c.execute("SELECT * FROM tasks"):
    print(row)

    
(1, 'My first task', 1)
(2, 'My new task', 15)
(3, 'My second task', 5)
(4, 'My third task', 10)

c.execute("SELECT * FROM tasks")
<sqlite3.Cursor object at 0x00000195FA2083C0>
rows = c.fetchall()
for row in rows:
   print(row)

   
(1, 'My first task', 1)
(2, 'My new task', 15)
(3, 'My second task', 5)
(4, 'My third task', 10)

c.execute("SELECT * FROM tasks")
<sqlite3.Cursor object at 0x00000195FA2083C0>
row = c.fetchone()
print(row)
(1, 'My first task', 1)

row = c.fetchone()
print(row)
(2, 'My new task', 15)

>>> c.execute("UPDATE tasks SET priority = ? WHERE id = ?", (20, 1))
<sqlite3.Cursor object at 0x00000195FA2083C0>
>>> conn.commit()
>>> 
>>> c.execute("DELETE FROM tasks WHERE id = ?", (1,))
<sqlite3.Cursor object at 0x00000195FA2083C0>
>>> conn.commit()
>>> conn.close()
>>> 
>>> 
>>> with sqlite3.connect("todo.db") as conn:
...     with conn.cursor() as c:
...        c.execute("""CREATE TABLE IF NOT EXISTS tasks (
...         id INTEGER PRIMARY KEY,
...         name TEXT NOT NULL,
...         priority INTEGER NOT NULL
...         );""")
... 
...        
Traceback (most recent call last):
  File "<pyshell#41>", line 2, in <module>
    with conn.cursor() as c:
TypeError: 'sqlite3.Cursor' object does not support the context manager protocol
>>> with sqlite3.connect("todo.db") as conn:
...     with conn.cursor() as c:
...        c.execute("""CREATE TABLE IF NOT EXISTS tasks (
...         id INTEGER PRIMARY KEY,
...         name TEXT NOT NULL,
...         priority INTEGER NOT NULL
...         );""")
...        c.execute("INSERT INTO tasks (name, priority) VALUES (?,?)", ("My first task", 1))
...        conn.commit()
... 
...        
Traceback (most recent call last):
  File "<pyshell#45>", line 2, in <module>
    with conn.cursor() as c:
TypeError: 'sqlite3.Cursor' object does not support the context manager protocol
