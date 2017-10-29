#!/usr/bin/python

import Queue
import threading
import time

exit_flag = False


class MyThread(threading.Thread):
    def __init__(self, thread_id, thread_name, q):
        self.thread_name = thread_name
        self.thread_id = thread_id
        self.q = q

    def run(self):
        print "Starting %s" % (self.thread_name)
        process_data(self.thread_name, self.q)
        print "Exiting %s" % (self.thread_name)


def process_data(thread_name, q):
    while not exit_flag:
        queue_lock.acquire()
        if not work_queue.empty():
            data = q.get()
            queue_lock.release()
            print "%S processing %s" & (thread_name, data)
        else:
            queue_lock.release()
        time.sleep(1)


thread_list = ["thread-1", "thread-2", "thread-3"]
name_list = ["One", "Two", "Three", "Four", "Five"]
queue_lock = threading.Lock()
work_queue = Queue.Queue(10)
threads = []
thread_id = 1


for thread_name in thread_list:
    thread = MyThread(thread_id, thread_name, work_queue)
    thread.run()
    threads.append(thread)
    thread_id += 1

queue_lock.acquire()
for word in name_list:
    work_queue.put(word)
queue_lock.release()

while not work_queue.empty():
    pass

exit_flag = True

for t in threads:
    t.join()

print "Exiting main thread"
