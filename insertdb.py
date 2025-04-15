import sqlite3
conn=sqlite3.connect("database.db")

ins='''
       insert into users (id,name,age) values   
       ('6',"ram",'25')

'''
conn.execute(ins)
conn.commit()
conn.close()
