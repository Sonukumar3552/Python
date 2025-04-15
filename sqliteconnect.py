import sqlite3
conn=sqlite3.connect("sqlite.db")
conn.execute('''
       create table student(
             st_id INT AUTO_INCREAMENT PRIMARY KEY,
             st_name VARCHAR(50),
             st_class VARCHAR(10),
             st_email VARCHAR(30))
''')
conn.close()