"""
Homework 7 Exercise 2
Name: Alejandro Diaz
Due Date: 12/08/23

Exercise 2:
The famous Fibonacci Sequence is the series of numbers like this:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The next number is found by adding up the two numbers prior to it.
- 2 is found by adding the two numbers before it (1+1)
- 3 is found by adding the two numbers before it (1+2),
- 5 is (2+3),
- ......

An implementation could be like this:

    def fibonacci(num):
        if num < 2:
            return num
        return fibonacci(num - 1) + fibonacci(num - 2)

But the runtime performance is terrible. This is because the code keeps recalculating
Fibonacci numbers that are already known.

    1. Implement a @cache decorator that will save the calculations in
       a function attribute dictionary. Even though the function
       fibonacci(num) only has one input argument, please make the
       decorator work for functions with any number of arguments (the
       decorator's own arguments can be ignored).

    2. Apply the @countCalls decorator introduced in class to the fibonacci function.
       Do you see a difference between using @cache and not using it
       (hint: use nested decorator)?

       Write your conclusion at the top of your code, in the multiline comment under
       “Description of your program”

Conclusion:
The fibonacci function using the decorator is way faster
than the one without it.
"""


import functools
import time


# CountCalls function decorator:
def countCalls(func):
    @functools.wraps(func)
    def wrapperCountCalls(*args, **kwargs):
        wrapperCountCalls.numCalls += 1
        print("Call {} of {}".format(wrapperCountCalls.numCalls, func.__name__))
        return func(*args, **kwargs)

    wrapperCountCalls.numCalls = 0
    return wrapperCountCalls


# Cache function decorator:
def cache(func):
    def wrapper(*args):
        if args in fib_dict:
            return fib_dict[args]
        else:
            value = func(*args)
            fib_dict[args] = value
            return value

    fib_dict = {}
    return wrapper


@countCalls
@cache
def fibonacci_new(num=1):
    if num < 2:
        return num
    return fibonacci_new(num - 1) + fibonacci_new(num - 2)


@countCalls
def fibonacci_old(num=1):
    if num < 2:
        return num
    return fibonacci_old(num - 1) + fibonacci_old(num - 2)


def time_this(function):
    start = time.time()
    function()
    end = time.time()

    print('TOTAL: {0:.7f} seconds'.format(end-start))


if __name__ == '__main__':
    var = 10

    # Printing the fibonacci sequence execution times:
    print("AY FIBO, HIT THE SEQUENCE!")

    print("\nFUNCTION: New fibonacci function")
    time_this(lambda: fibonacci_new(var))

    # Sleep for 2 seconds before printing old fibo stats:
    time.sleep(2)

    print("\nFUNCTION: Old fibonacci function")
    time_this(lambda: fibonacci_old(var))
