import threading
import sqlite3
import time

rows = []

def read_from_sql(dbName):
    global rows
    con_obj = sqlite3.connect(dbName)
    cur_obj = con_obj.cursor()
    query = """SELECT * FROM players"""
    cur_obj.execute(query)
    rows = cur_obj.fetchall()
    con_obj.close()

def write_into_file(fileName):
    time.sleep(0.1)
    fa = open(fileName, "w")
    for row in rows:
        for val in row:
            fa.write(str(val) + " ")
            time.sleep(0.1)
        fa.write("\n")
#    fa.close()

def read_data_from_file(fileName):
    time.sleep(1)
    print('contents in the file:')
    with open(fileName, "r") as fa:
        stra = fa.read()
        print(stra)

ta = threading.Thread(target=read_from_sql, args=('sports.db', ))
tb = threading.Thread(target=write_into_file, args=('players.txt', ))
tc = threading.Thread(target=read_data_from_file, args=('players.txt', ))

ta.start()
tb.start()
tc.start()

ta.join()
tb.join()
tc.join()

time.sleep(2)
print("exiting the application")








#
