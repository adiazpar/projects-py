"""
Homework 6 Exercise 3
Name: Alejandro Diaz
Due Date: 11/26/23

Exercise 3:
Write a multithreading program that:

    1. In your main thread
        A. Ask the user to enter an integer as the total number of threads. Name this integer numThreads;
        B. If the user enters a non-integer (e.g., a float or a string) or an integer smaller than 2,
           keep asking the user to re-enter until the input is an integer >= 2;

    2. In your main thread
        A. Create numThreads threads using a function called someFunc(i) in a for loop;
        B. When created, each thread is passed an argument i that is the control variable of the for loop;
        C. After creating these threads, use join() to wait for all threads to finish in a separate for loop;

    3. In each of the new thread created using someFunc(i), use the logging module to print all the messages
       with the following format, using the logging.DEBUG level:
        A. human-readable time – line number where message is printed – the actual

    4. In each of the new thread created
        A. Print “Welcome thread i” (where i is the argument passed in; please print i’s actual value);
        B. Print whether the number i is even or odd;
        C. Sleep for 3 seconds;
        D. Print “Goodbye thread i” (please print i’s actual value);

For example, if numThreads is 6, an example output could look like the following (but will not be exactly the same):

    2023-11-09 11:04:55,143 - 10 - Welcome thread 0
    2023-11-09 11:04:55,144 - 12 - Number 0 is even
    2023-11-09 11:04:55,144 - 10 - Welcome thread 1
    2023-11-09 11:04:55,144 - 14 - Number 1 is odd
    2023-11-09 11:04:55,144 - 10 - Welcome thread 2
    2023-11-09 11:04:55,145 - 12 - Number 2 is even
    2023-11-09 11:04:55,145 - 10 - Welcome thread 3
    2023-11-09 11:04:55,146 - 14 - Number 3 is odd
    2023-11-09 11:04:55,146 - 10 - Welcome thread 4
    2023-11-09 11:04:55,146 - 12 - Number 4 is even
    2023-11-09 11:04:55,147 - 10 - Welcome thread 5
    2023-11-09 11:04:55,147 - 14 - Number 5 is odd
    2023-11-09 11:04:58,147 - 16 - Goodbye thread 0
    2023-11-09 11:04:58,148 - 16 - Goodbye thread 2
    2023-11-09 11:04:58,148 - 16 - Goodbye thread 1
    2023-11-09 11:04:58,149 - 16 - Goodbye thread 4
    2023-11-09 11:04:58,149 - 16 - Goodbye thread 3
    2023-11-09 11:04:58,149 - 16 - Goodbye thread 5
"""

import threading
import time
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(lineno)d - %(message)s')


def someFunc(i):
    # Debugging:
    logging.debug("Welcome thread ({})".format(i))
    if i % 2 == 0:
        logging.debug("Number ({}) is even".format(i))
    else:
        logging.debug("Number ({}) is odd".format(i))

    time.sleep(3)
    logging.debug("Goodbye thread ({})".format(i))


if __name__ == "__main__":
    # Prompt the user to enter the total number of threads to run:
    valid = False
    numThreads = 0

    # Validate the user input
    while not valid:
        print('Please enter the max amount of threads to run: ', end='')
        temp = input()

        if temp.isdigit():
            num_val = int(temp)

            if num_val > 1:
                numThreads = num_val
                valid = True

    # Creating numThreads amount of threads:
    threads = [None] * numThreads

    for i in range(len(threads)):
        threads[i] = threading.Thread(target=someFunc, args=(i,))
        threads[i].start()

    # Joining all the threads in a seperate for loop:
    [thread.join() for thread in threads]

    # Confirm when threads are finished:
    print("\nEnd of program.")
