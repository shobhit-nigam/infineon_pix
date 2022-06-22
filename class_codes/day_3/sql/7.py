import sqlite3
import time

con_obj = sqlite3.connect('sports.db')
cur_obj = con_obj.cursor()

lista = [[282, "Sunil Chhetri", "soccer", 3420.24],
        [284, "Kapil Dev", "all rounder", 5678],
        [288, "PV Sindhu", "shuttler", 34720],
        [290, "abhinav Bindra", "shooter", 24678]]


query = """INSERT into players (id, name, skill, price) VALUES(?,?,?,?)"""

cur_obj.executemany(query, lista)

con_obj.commit()

con_obj.close()
