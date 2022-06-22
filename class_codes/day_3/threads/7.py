import time
import threading

def taska():
    for i in range(3, 0, -1):
        print(f"task A will finish in {i} seconds")
        time.sleep(1)

def taskb():
    for i in range(30, 0, -1):
        print(f"task B will finish in {i} seconds")
        time.sleep(1)

ta = threading.Thread(target=taska)
tb = threading.Thread(target=taskb)

tb.setDaemon(True)
ta.start()
tb.start()

for i in range(6, 0, -1):
    print(f"main task will finish in {i} seconds")
    time.sleep(1)

tb.join(12.0)

print("last line")
