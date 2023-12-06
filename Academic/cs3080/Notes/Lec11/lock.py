# Threads with a lock
import threading
import time

print('Start of program.')
myList = []
# create a lock
lock = threading.Lock()


def func(i):
    #time.sleep(1)
    # acquire the lock
    lock.acquire()

    myList.append(i)
    # id of list: id(myList)
    print('    Start doing something in thread {}, '
          'with list {} (at {})'.format(i, myList, id(myList)))
    time.sleep(1)
    # I want thread i to read back the same myList
    print('    Thread {} finished with list {}'.format(i, myList))

    # release the lock
    lock.release()


threads = [None] * 5
for i in range(len(threads)):
    threads[i] = threading.Thread(target=func, args=(i,))
    threads[i].start()


[thread.join() for thread in threads]
print('End of program.')

