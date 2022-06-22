import sqlite3
import time

con_obj = sqlite3.connect('sports.db')
cur_obj = con_obj.cursor()

lista = [280, "Mithali Raj", "batter", 3468.24]


query = """INSERT into players (id, name, skill, price) VALUES(?,?,?,?)"""

cur_obj.execute(query, lista)

con_obj.commit()

con_obj.close()
