import sys
import time
import os

class Monitor:

    def __init__(self, fileName):
        self.fileName = fileName
        self.prev_stamp = os.stat(self.fileName).st_mtime

    def look(self):
        cur_stamp = os.stat(self.fileName).st_mtime
        if cur_stamp != self.prev_stamp:
            self.prev_stamp = cur_stamp
            print("File has changed")

    def watch(self):
        while True:
            try:
                time.sleep(1)
                self.look()
            except FileNotFoundError:
                print(f"no such file as {self.fileName}, please check again")
                break
            except:
                print("unknown issue --> ", sys.exc-info()[0])

file = input("enter the file name to be monitored:\n")
print("starting the monitoring for file -->", file)

objs = Monitor(file)
objs.watch()



























#
