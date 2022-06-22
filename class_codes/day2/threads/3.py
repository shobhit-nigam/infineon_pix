import time
import threading

def taska(num):
    for i in range(3, 0, -1):
        print(f"task A will finish in {i} seconds and has num = {num}")
        time.sleep(1)

def taskb(num):
    for i in range(6, 0, -1):
        print(f"task B will finish in {i} seconds and has num = {num}")
        time.sleep(1)

ta = threading.Thread(target=taska, args=(11,))
tb = threading.Thread(target=taskb, args=(21,))

ta.start()
tb.start()

for i in range(9, 0, -1):
    print(f"main task will finish in {i} seconds")
    time.sleep(1)
