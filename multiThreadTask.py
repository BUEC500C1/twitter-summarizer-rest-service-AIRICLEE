import time
import queue
import threading
import sys
from getTwits import *


def worker(i):
    while True:
        qEle = q.get()
        if qEle is None:
            print("Thread %s find the object None, now it can take a rest ^-^" % i)
            break

        # execute do_work(item)
        time.sleep(0.5)
        getResult(qEle[0], qEle[1])
        print("Thread %s hava finished the task <%s> ！" % (i, qEle[0]))
        
        # After finish this task, return the signal
        q.task_done()


if __name__ == '__main__':
    num_of_threads = 2

    # source = ['Jackson', 'Vincent', 'Lee', 'EC_500_Staff', 'Osama', 'TA', 'Admin']
    source = ['Jackson', 'Vincent', 'Lee']

    # create queue
    q = queue.Queue()
    
    # build threads pool
    threads = []
    
    # create thread, and put them into pools
    for i in range(1, num_of_threads+1):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.daemon = True
        t.start()

    # put the task into queue
    for item in source:
        time.sleep(0.5)     # each 0.5s launch a new task
        qEle = []
        qEle.append(item)
        qEle.append(sys.argv[1])
        q.put(qEle)


    q.join()
    print("-----All the task have been finished-----")
    # stop the working thread
    for i in range(num_of_threads):
        q.put(None)
    for t in threads:
        t.join()