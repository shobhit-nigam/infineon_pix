import threading

objl = threading.RLock()

def funca():
    print("first try : ", objl.acquire())

def funcb():
    # re-acquire
    print("second try :", objl.acquire())

def mainTask():
    funca()
    # code executes
    funcb()
    print("last line")
    objl.release()

mainTask()
