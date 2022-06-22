import time
import threading

def funca():
    print("hello wednesday")

ta = threading.Timer(4.0, funca)
ta.start()
