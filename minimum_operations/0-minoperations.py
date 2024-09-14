#!/usr/bin/python3
"""In a text file, you start with a single character 'H'.The text editor 
allows only two actions: "Copy All" and "Paste".Given a number n, create 
a method to determine the minimum number of operations required to 
produce exactly n 'H' characters in the file
"""


def minOperations(n):
    if n < 2:
        return 0

    current_num_of_h = 1
    copied = 0
    num_of_operations = 0

    while current_num_of_h < n:
        if n % current_num_of_h == 0:
            copied = current_num_of_h
            num_of_operations += 1

        current_num_of_h += copied
        num_of_operations += 1
    return num_of_operations
