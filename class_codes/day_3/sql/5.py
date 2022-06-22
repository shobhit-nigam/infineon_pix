import sqlite3
import time

con_obj = sqlite3.connect('sports.db')
cur_obj = con_obj.cursor()

query = """CREATE TABLE players(id integer PRIMARY KEY, name text,
            skill text, price real)"""

cur_obj.execute(query)

con_obj.close()
