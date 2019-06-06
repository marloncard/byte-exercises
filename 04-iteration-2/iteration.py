def my_loop(x):
    # Iterate over range 0 to x and print each item
    for i in range(x):
        print(i)


def my_reverse_loop(y):
    # Starting at y print y then reduce value by one until zero
    y -= 1
    while y > -1:
        print(y)
        y -= 1

print (my_loop(10))
print(my_reverse_loop(10))
