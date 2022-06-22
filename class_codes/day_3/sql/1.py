import sqlite3

con_obj = sqlite3.connect('chinook.db')
cur_obj = con_obj.cursor()

query = """SELECT * FROM employees"""
cur_obj.execute(query)

rows = cur_obj.fetchall()

print("num of records =", len(rows))
print("----")
print(rows)

con_obj.close()
