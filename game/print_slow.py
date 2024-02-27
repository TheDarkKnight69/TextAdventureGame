import time


def print_slow(string):
    for i in string:
        print(i, end="")
        time.sleep(0.2)
