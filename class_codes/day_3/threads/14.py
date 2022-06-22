import threading

objl = threading.Lock()

def funca():
    print("first try : ", objl.acquire())

def funcb():
    print("second try :", objl.acquire())

def mainTask():
    funca()
    # code executes
    funcb()
    print("last line")
    objl.release()

mainTask()
