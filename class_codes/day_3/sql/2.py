import sqlite3
import time

con_obj = sqlite3.connect('chinook.db')
cur_obj = con_obj.cursor()

query = """SELECT * FROM employees"""
cur_obj.execute(query)

rows = cur_obj.fetchall()

print("num of records =", len(rows))
print("----")

for record in rows:
    print(record)
    time.sleep(2)


con_obj.close()
