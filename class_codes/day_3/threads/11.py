import time
import threading

# shared resource
ga = 0
objl = threading.Lock()

def taska():
    global ga
    global objl
    print("task a asking for lock")
    objl.acquire()
    ga = ga + 1
    print("starting task", ga)
    for i in range(10):
        print(end="")
    time.sleep(6)
    print("ending task", ga)
    print("task a releasing the lock")
    objl.release()

def taskb():
    global ga
    global objl
    print("task b asking for lock")
    objl.acquire()
    ga = ga + 1
    print("starting task", ga)
    for i in range(10):
        print(end="")
    time.sleep(2)
    print("ending task", ga)
    print("task b releasing the lock")
    objl.release()

ta = threading.Thread(target=taska)
tb = threading.Thread(target=taskb)

ta.start()
tb.start()
