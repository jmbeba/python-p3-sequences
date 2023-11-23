#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci = list()
    for i in range(length):
        if (i == 0):
            fibonacci.append(0)
        elif (i == 1):
            fibonacci.append(1)
        else:
            fibonacci.append((fibonacci[i-1] + fibonacci[i-2]))

    print(fibonacci)