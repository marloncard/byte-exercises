#!/usr/bin/env python3

"""
* Write a function that will take a number as an argument.
* The function will loop from 0 to the number.
* If the number is divisible by 3 print `Fizz` to the terminal.
* If the number is divisible by 5 print `Buzz` to the terminal.
* if the number is divisible by 3 and 5 print `FizzBuzz` to the terminal.
"""

def fizzbuzz(arg):
    # TODO Loop from zero to arg
    for i in range(len(arg)):
    # If arg % 3 == 0 and arge % 5 == 0 print 'FizzBuzz'
        if arg[i] % 3 == 0 and arg[i] % 5 == 0:
            print('FizzBuzz')
    # If arg % 3 == 0 print 'Fizz'
        elif arg[i] % 3 == 0:
            print('Fizz')
    # If arg % 5 == 0 print 'Buzz'
        elif arg[i] % 5 == 0:
            print('Buzz')
        else:
            print(arg[i])


print(fizzbuzz([15, 30, 17, 18, 21, 55]))