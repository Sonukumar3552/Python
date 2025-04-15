import sqlite3
conn=sqlite3.connect("sqlite.db")
st_id=input("enter the student id:-")
conn.execute("delete from student where st_id="+st_id)
conn.close()