#!/usr/local/bin/python3

import threading
import time
import sys

print(sys.version)

exit_flag = False


class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting "+self.name
        print_time(self.name, self.counter, 5)
        print "Exiting "+self.name


def print_time(thread_name, counter, delay):
    while counter:
        if exit_flag:
            thread_name.exit()
        time.sleep(delay)
        print "%s %s" % (thread_name, time.ctime(time.time()))
        counter -= 1


thread_1 = MyThread(1, "Thread-1", 5)
thread_2 = MyThread(2, "Thread-2", 3)

thread_1.start()
thread_2.start()

print "Exiting main thread"