import time
import threading

def taska(obje):
    print("wait for the event, starting")
    event_set = obje.wait()
    print("event set -->", event_set)

def wait_event_timeout(obje, t):
    while not obje.isSet():
        print("wait for event timeout, starting")
        event_set = obje.wait(t)
        print("event set -->", event_set)
        if event_set:
            print("processing event")
        else:
            print("executing other parts")

obje = threading.event()
ta = threading.Thread(target=taska, args =(obje,))
tb = threading.Thread(target=wait_event_timeout, args =(obje, 2))

ta.start()
tb.start()
