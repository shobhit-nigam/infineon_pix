import sqlite3
import time

con_obj = sqlite3.connect('sports.db')
cur_obj = con_obj.cursor()

query = """UPDATE players SET name = "Abhinav Bindra" where id = 290"""

cur_obj.execute(query)

con_obj.commit()

con_obj.close()
