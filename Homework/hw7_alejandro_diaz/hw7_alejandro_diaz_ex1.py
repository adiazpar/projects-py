"""
Homework 7 Exercise 1
Name: Alejandro Diaz
Due Date: 12/08/23

Exercise 1:
Write a @slowDown decorator that will sleep for a certain number of seconds before it
calls the decorated function. Use an optional rate argument for the decorator that controls
how long (in seconds) it sleeps.

Use a default value of 1 second for the sleep duration. Note that you can modify the
@slowDown example provided in class by letting the decorator accept an argument that is the
number of seconds to sleep, and then use the same recursive countdown(fromNumber) as the
function to decorate and test the decorator.
"""

import functools
import time


def slowDown(func):
    # Sleep for a (rate) amount of seconds before calling decorated function:
    @functools.wraps(func)
    def wrapper(countDownNum, rate=1):
        time.sleep(rate)
        return func(countDownNum, rate)

    return wrapper


@slowDown
def countDown(fromNumber, rate=1):
    if fromNumber >= 1:
        print(fromNumber)
        countDown(fromNumber - 1, rate)
    else:
        print("!!! KABOOM !!!")


if __name__ == "__main__":
    countDown(5)