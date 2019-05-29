#!/usr/bin/env python3

"""
* Write a function that takes in a float as an argument
* This function should return the number of American coins and bills needed to represent that float. (Round to the nearest penny)

Use the following denominations:

    Penny: 1 cent
    Nickel: 5 cent
    Dime: 10 cent
    Quarter: 25 cent
    One-dollar bill
    Five-dollar bill
    Ten-dollar bill
    Fifty-dollar bill
    Hundred-dollar bill

input: Float

Example - 
output:
```
[input]
currency_converter(12.33)

[output]
1 $10
2 $1
1 quarter
1 nickel
3 penny
```

"""


currency = {'hundred': 100,
            'fifty': 50,
            'ten': 10,
            'five': 5,
            'one': 1,
            'quarter': .25,
            'dime': .10,
            'nickel': .05,
            'penny': .01}

def currency_converter(amount):
# Iterate over currency dict
    for key, value in currency.items():
        # If amount divided by currency_item not < 0;
        if amount / value > 0:
            # Omit any zero results
            if amount // value > 0:
                # Print amount // currency_item => (print('{:.2f}'.format(amount)))
                print('{:.0f}'.format(amount // value) + ' ' + key)
                # amount = amount % currency_item
                amount = amount % value

    
currency_converter(2345.18)