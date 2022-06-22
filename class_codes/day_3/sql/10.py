import threading
import sqlite3
import time

rows = []
objl = threading.Lock()

def read_from_sql(dbName):
    objl.acquire()
    global rows
    print("reading from sql begins")
    con_obj = sqlite3.connect(dbName)
    cur_obj = con_obj.cursor()
    query = """SELECT * FROM players"""
    cur_obj.execute(query)
    rows = cur_obj.fetchall()
    con_obj.close()
    print("reading from SQL complete")
    objl.release()


def write_into_file(fileName):
    print("writing into file will begin")
    objl.acquire()
    with open(fileName, "w") as fa:
        for row in rows:
            for val in row:
                fa.write(str(val) + " ")
                time.sleep(0.1)
            fa.write("\n")
    print("writing into file complete")
    objl.release()
    return fa

def read_data_from_file(fileName):
    time.sleep(0.1)
    objl.acquire()
    print("reading from file begins")
    print('contents in the file:')
    fa = open(fileName, "r")
    stra = fa.read()
    print(stra)
    fa.close()
    objl.release()
    return fa

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
