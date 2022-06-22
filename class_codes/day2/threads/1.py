import time

def taska():
    for i in range(3, 0, -1):
        print(f"task A will finish in {i} seconds")
        time.sleep(1)

def taskb():
    for i in range(6, 0, -1):
        print(f"task B will finish in {i} seconds")
        time.sleep(1)

taska()
taskb()
for i in range(9, 0, -1):
    print(f"main task will finish in {i} seconds")
    time.sleep(1)
