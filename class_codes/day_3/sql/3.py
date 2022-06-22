import sqlite3
import time
import pandas as pd

con_obj = sqlite3.connect('chinook.db')

query = """SELECT * FROM employees"""

dfa = pd.read_sql_query(query, con_obj)

print(dfa)
print("-----")
print(list(dfa['FirstName']))

con_obj.close()
