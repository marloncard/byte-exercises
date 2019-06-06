#!/usr/bin/env python3
"""
* Create a variable and assign it to the array below


[2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]

* Write a function that will take in this variable
* It will return the median number in the array
* It will return the average of that array
* It will return the number that occurs most frequently in the array

Please see the example `input` and `output` below.


[input]
[2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]

[output]
9
14
8

"""

number_list = [2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]

def iteration_three(arg):
    # Sort list in place
    arg.sort()
    # Median number is at index location: total index / 2
    print(arg[len(arg)//2])
    # Average is array total / array length
    print(sum(arg)//len(arg))
    # Iterate over list values
    max_counts = 0
    max_value = None

    for i in arg:
        # If the count of item in list is > max_counts, max_value is item
        if arg.count(i) > max_counts:
            max_counts = arg.count(i)
            max_value = i

    # TODO max_value = map(lamda x: arg.count(x) > max_counts, arg)
    print(max_value)

if __name__ == "__main__":
    iteration_three(number_list)
