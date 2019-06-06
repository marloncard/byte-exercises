#!/usr/bin/env python3

"""
* Write a function that will take a number as an argument.
* The function will loop from 0 to the number.
* If the number is divisible by 3 print `Fizz` to the terminal.
* If the number is divisible by 5 print `Buzz` to the terminal.
* if the number is divisible by 3 and 5 print `FizzBuzz` to the terminal.
"""

def fizzbuzz(arg):
    # Loop from zero to arg
    for i in range(arg):
    # If modulo of 3 and 5 is zero, print 'FizzBuzz'
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
    # If modulo of only 3 is zero print 'Fizz'
        elif i % 3 == 0:
            print('Fizz')
    # If modulo of only 5 is zero print 'Buzz'
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)


print(fizzbuzz(55))
