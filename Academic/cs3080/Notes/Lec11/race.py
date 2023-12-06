# Threads with a race condition
import threading
import time

print('Start of program.')
myList = []


def raceFunc(i):
    myList.append(i)
    # id of list: id(myList)
    print('    Start doing something in thread {}, '
          'with list {} (at {})'.format(i, myList, id(myList)))
    time.sleep(1)
    # I want thread i to read back the same myList
    print('    Thread {} finished with list {}'.format(i, myList))


threads = [None] * 5
for i in range(len(threads)):
    threads[i] = threading.Thread(target=raceFunc, args=(i,))
    threads[i].start()

# do some other stuff
print()   # print an empty line

[thread.join() for thread in threads]
print('End of program.')
