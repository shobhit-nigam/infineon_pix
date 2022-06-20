val = 30

class AppException(Exception):
    """parent class for all exceptions in the app"""
    pass

class TooSmall(AppException):
    def __init__(self):
        print("too small a value")

class TooLarge(AppException):
    def __init__(self):
        print("too Large a value")

while True:
    try:
        num = int(input("enter a number: \n"))
        if num < val:
            raise TooSmall
        elif num > val:
            raise TooLarge
        else:
            print("correct guess")
            break
    except TooSmall:
        pass
    except TooLarge:
        pass
