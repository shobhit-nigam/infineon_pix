import threading
import time

class BlockQueue:
    def __init__(self, max):
        self.max_size = max
        self.cur_size = 0
        self.cond = threading.Condition()
        self.q = []
        pass

    def enqueue(self, data):
        self.cond.acquire()
        while self.cur_size == self.max_size:
            self.cond.wait()

        self.q.append(data)
        self.cur_size = self.cur_size + 1
        self.cond.notifyAll()
        print(f"current size of queue is {self.cur_size}, and the queue is --> {self.q}")
        self.cond.release()
        pass

    def dequeue(self):
        self.cond.acquire()
        while self.cur_size == 0:
            self.cond.wait()

        data = self.q.pop(0)
        self.cur_size = self.cur_size - 1
        self.cond.notifyAll()
        self.cond.release()
        return data

def taking_thread(q):
    while True:
        data = q.dequeue()
        print(f"{threading.current_thread().getName()}, consumed item {data}")
        time.sleep(5)

def putting_thread(q, val):
    data = val
    while True:
        q.enqueue(data)
        data = data + 2
        time.sleep(0.1)

objB = BlockQueue(5)

taking_ta = threading.Thread(target=taking_thread, name="taking_ta", daemon=True, args=(objB,))
taking_tb = threading.Thread(target=taking_thread, name="taking_tb", daemon=True, args=(objB,))
putting_ta = threading.Thread(target=putting_thread, name="putting_ta", daemon=True, args=(objB, 13))
putting_tb = threading.Thread(target=putting_thread, name="putting_tb", daemon=True, args=(objB, 100))



taking_ta.start()
taking_tb.start()
putting_ta.start()
putting_tb.start()

time.sleep(30)
print("main thread will exit")

#
